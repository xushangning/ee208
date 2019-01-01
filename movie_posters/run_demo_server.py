#!/usr/bin/env python3

from pathlib import Path
import os

import time
import datetime
import cv2
import numpy as np
import uuid
import json

import functools
import logging
import collections

from pytesseract import image_to_string

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@functools.lru_cache(maxsize=1)
def get_host_info():
    ret = {}
    with open('/proc/cpuinfo') as f:
        ret['cpuinfo'] = f.read()

    with open('/proc/meminfo') as f:
        ret['meminfo'] = f.read()

    with open('/proc/loadavg') as f:
        ret['loadavg'] = f.read()

    return ret


@functools.lru_cache(maxsize=100)
def get_predictor(checkpoint_path):
    logger.info('loading model')
    import tensorflow as tf
    import model
    from icdar import restore_rectangle
    import lanms
    from eval import resize_image, sort_poly, detect

    input_images = tf.placeholder(tf.float32, shape=[None, None, None, 3], name='input_images')
    global_step = tf.get_variable('global_step', [], initializer=tf.constant_initializer(0), trainable=False)

    f_score, f_geometry = model.model(input_images, is_training=False)

    variable_averages = tf.train.ExponentialMovingAverage(0.997, global_step)
    saver = tf.train.Saver(variable_averages.variables_to_restore())

    sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))

    ckpt_state = tf.train.get_checkpoint_state(checkpoint_path)
    model_path = os.path.join(checkpoint_path, os.path.basename(ckpt_state.model_checkpoint_path))
    logger.info('Restore from {}'.format(model_path))
    saver.restore(sess, model_path)

    def predictor(img):
        """
        :return: {
            'text_lines': [
                {
                    'score': ,
                    'x0': ,
                    'y0': ,
                    'x1': ,
                    ...
                    'y3': ,
                }
            ],
            'rtparams': {  # runtime parameters
                'image_size': ,
                'working_size': ,
            },
            'timing': {
                'net': ,
                'restore': ,
                'nms': ,
                'cpuinfo': ,
                'meminfo': ,
                'uptime': ,
            }
        }
        """
        start_time = time.time()
        rtparams = collections.OrderedDict()
        rtparams['start_time'] = datetime.datetime.now().isoformat()
        rtparams['image_size'] = '{}x{}'.format(img.shape[1], img.shape[0])
        timer = collections.OrderedDict([
            ('net', 0),
            ('restore', 0),
            ('nms', 0)
        ])

        im_resized, (ratio_h, ratio_w) = resize_image(img)
        rtparams['working_size'] = '{}x{}'.format(
            im_resized.shape[1], im_resized.shape[0])
        start = time.time()
        score, geometry = sess.run(
            [f_score, f_geometry],
            feed_dict={input_images: [im_resized[:,:,::-1]]})
        timer['net'] = time.time() - start

        boxes, timer = detect(score_map=score, geo_map=geometry, timer=timer)
        logger.info('net {:.0f}ms, restore {:.0f}ms, nms {:.0f}ms'.format(
            timer['net']*1000, timer['restore']*1000, timer['nms']*1000))

        if boxes is not None:
            scores = boxes[:,8].reshape(-1)
            boxes = boxes[:, :8].reshape((-1, 4, 2))
            boxes[:, :, 0] /= ratio_w
            boxes[:, :, 1] /= ratio_h

        duration = time.time() - start_time
        timer['overall'] = duration
        logger.info('[timing] {}'.format(duration))

        text_lines = []
        if boxes is not None:
            text_lines = []
            for box, score in zip(boxes, scores):
                box = sort_poly(box.astype(np.int32))
                if np.linalg.norm(box[0] - box[1]) < 5 or np.linalg.norm(box[3]-box[0]) < 5:
                    continue
                tl = collections.OrderedDict(zip(
                    ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3'],
                    map(float, box.flatten())))
                tl['score'] = float(score)
                text_lines.append(tl)
        ret = {
            'text_lines': text_lines,
            'rtparams': rtparams,
            'timing': timer,
        }
        ret.update(get_host_info())
        return ret


    return predictor


### the webserver
from flask import Flask, request, render_template
import argparse


class Config:
    SAVE_DIR = 'static/results'


config = Config()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', session_id='dummy_session_id')


def draw_illu(illu, rst):
    for t in rst['text_lines']:
        d = np.array([t['x0'], t['y0'], t['x1'], t['y1'], t['x2'],
                      t['y2'], t['x3'], t['y3']], dtype='int32')
        d = d.reshape(-1, 2)
        cv2.polylines(illu, [d], isClosed=True, color=(255, 255, 0))
    return illu


def save_result(img, rst):
    session_id = str(uuid.uuid1())
    dirpath = os.path.join(config.SAVE_DIR, session_id)
    os.makedirs(dirpath)

    # save input image
    output_path = os.path.join(dirpath, 'input.png')
    cv2.imwrite(output_path, img)

    # save illustration
    output_path = os.path.join(dirpath, 'output.png')
    cv2.imwrite(output_path, draw_illu(img.copy(), rst))

    # save json data
    output_path = os.path.join(dirpath, 'result.json')
    with open(output_path, 'w') as f:
        json.dump(rst, f)

    rst['session_id'] = session_id
    return rst


@app.route('/', methods=['POST'])
def index_post():
    global predictor
    import io
    bio = io.BytesIO()
    request.files['image'].save(bio)
    img = cv2.imdecode(np.frombuffer(bio.getvalue(), dtype='uint8'), 1)
    rst = get_predictor(checkpoint_path)(img)

    save_result(img, rst)
    return render_template('index.html', session_id=rst['session_id'])


def main():
    global checkpoint_path
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=8769, type=int)
    parser.add_argument('--checkpoint_path', default=checkpoint_path)
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    checkpoint_path = args.checkpoint_path

    if not os.path.exists(args.checkpoint_path):
        raise RuntimeError(
            'Checkpoint `{}` not found'.format(args.checkpoint_path))

    app.debug = args.debug
    app.run('0.0.0.0', args.port)


def extract_rot(img, save_path):
    params = get_predictor(checkpoint_path)(img)
    cv2.imwrite(os.path.join(save_path, rot_filename),
                draw_illu(img.copy(), params))
    coordinates = params['text_lines']
    # handle coordinates that are out of the boundary of the image
    for c in coordinates:
        for i in range(4):
            x_key = 'x' + str(i)
            y_key = 'y' + str(i)
            if c[x_key] < 0:
                c[x_key] = 0
            elif c[x_key] > img.shape[1]:
                c[x_key] = img.shape[1]
            if c[y_key] < 0:
                c[y_key] = 0
            elif c[y_key] > img.shape[0]:
                c[y_key] = img.shape[0]
        c['angle'] = np.rad2deg(np.arctan(
            (c['y1'] - c['y0']) / (c['x1'] - c['x0'])))
        if abs(c['angle']) >= correction_threshold:
            c['text height'] = int(np.ceil(np.sqrt(
                (c['y3'] - c['y0']) ** 2 + (c['x3'] - c['x0']) ** 2)))
        else:
            upper_y = int(min(c['y0'], c['y1']))
            lower_y = int(max(c['y2'], c['y3']))
            c['text height'] = lower_y - upper_y
    coordinates.sort(key=lambda c: c['text height'], reverse=True)

    # only return 5 boxes with greatest height
    return coordinates[:5]


def recognize_text(img, box_coordinates, save_path):
    if len(box_coordinates) == 0:
        return

    rot_path = os.path.join(save_path, 'rot')
    if not os.path.exists(rot_path):
        os.mkdir(rot_path)
    f = open(os.path.join(save_path, recognized_text_filename), 'w')
    max_text_height = box_coordinates[0]['text height']
    for i, params in enumerate(box_coordinates):
        # only recognize the text if its height is within 70% of the greatest
        # text height
        if params['text height'] < max_text_height * 0.7:
            break
        if np.abs(params['angle']) >= correction_threshold:
            center = (params['x0'], params['y0'])
            # rotate around the center (x0, y0)
            M = cv2.getRotationMatrix2D(center, params['angle'], 1)
            # move center to the origin (x0, y0) -> (0, 0)
            M[0][2] -= center[0]
            M[1][2] -= center[1]
            # calculate text width as distance between (x0, y0) and (x1, y1),
            # text height as distance between (x0, y0) and (x3, y3)
            text_width = int(np.ceil(np.sqrt(
                (params['y1'] - params['y0']) ** 2 + (params['x1'] - params['x0']) ** 2)))
            rot = cv2.warpAffine(img, M, (text_width, params['text height']))
        else:
            left_x = int(min(params['x0'], params['x3']))
            right_x = int(max(params['x1'], params['x2']))
            upper_y = int(min(params['y0'], params['y1']))
            lower_y = int(max(params['y2'], params['y3']))
            rot = img[upper_y:lower_y, left_x:right_x]

        cv2.imwrite(os.path.join(rot_path, str(i) + '.png'), rot)
        text = image_to_string(rot, config=tesseract_options)
        f.write(text + '\n')
    f.close()


if __name__ == '__main__':
    checkpoint_path = './east_icdar2015_resnet_v1_50_rbox'
    dataset_path = 'dataset'
    result_path = 'results'
    rot_filename = 'rot.png'
    recognized_text_filename = 'suppressed_text.txt'
    # correct images with skew angles equal to or greater than 5 degrees
    correction_threshold = 5
    tesseract_options = '-l eng --oem 1 --psm 7'

    if not os.path.exists(result_path):
        os.mkdir(result_path)
    dataset_dir = Path(dataset_path)
    for f in dataset_dir.iterdir():
        print(f.name)
        movie_title = f.name.rstrip('.jpg')
        img = cv2.imread(str(f))
        result_save_path = os.path.join(result_path, movie_title)
        if not os.path.exists(result_save_path):
            os.mkdir(result_save_path)
        p = extract_rot(img, result_save_path)
        recognize_text(img, p, result_save_path)

    # main()
