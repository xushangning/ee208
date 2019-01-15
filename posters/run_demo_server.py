#!/usr/bin/env python3

from pathlib import Path
import os

import time
import datetime
import cv2
import numpy as np

import functools
import logging
import collections

from pytesseract import image_to_string

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

checkpoint_path = 'east_icdar2015_resnet_v1_50_rbox'
# correct images with skew angles equal to or greater than 5 degrees
correction_threshold = 5
tesseract_options = '-l eng --oem 1 --psm 7'


@functools.lru_cache(maxsize=1)
def get_host_info():
    # 原本为从 /proc 中读取系统信息，但 /proc 为 Linux 独有，所以将系统信息写死
    # 以解决系统兼容性问题。
    return {
        'cpuinfo': '''processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 158
model name	: Intel(R) Pentium(R) CPU G4560 @ 3.50GHz
stepping	: 9
microcode	: 0x8e
cpu MHz		: 2257.124
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 22
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov \
pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb \
rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology \
nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor \
ds_cpl vmx est tm2 ssse3 sdbg cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe \
popcnt tsc_deadline_timer aes xsave rdrand lahf_lm abm 3dnowprefetch cpuid_\
fault epb invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority \
ept vpid ept_ad fsgsbase tsc_adjust smep erms invpcid mpx rdseed smap \
clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm arat pln pts hwp \
hwp_notify hwp_act_window hwp_epp flush_l1d
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf
bogomips	: 7010.00
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:
''',
        'meminfo': '''MemTotal:        7925036 kB
MemFree:          223120 kB
MemAvailable:    4643672 kB
Buffers:          114532 kB
Cached:          4848936 kB
SwapCached:        40728 kB
Active:          3934840 kB
Inactive:        3383696 kB
Active(anon):    2060612 kB
Inactive(anon):   695680 kB
Active(file):    1874228 kB
Inactive(file):  2688016 kB
Unevictable:          96 kB
Mlocked:              96 kB
SwapTotal:      10485756 kB
SwapFree:       10099068 kB
Dirty:               132 kB
Writeback:             0 kB
AnonPages:       2348700 kB
Mapped:           871428 kB
Shmem:            401224 kB
KReclaimable:     169404 kB
Slab:             237016 kB
SReclaimable:     169404 kB
SUnreclaim:        67612 kB
KernelStack:       12032 kB
PageTables:        33632 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    14448272 kB
Committed_AS:    7274528 kB
VmallocTotal:   34359738367 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB
Percpu:             1344 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
DirectMap4k:      601760 kB
DirectMap2M:     7542784 kB
DirectMap1G:     1048576 kB
''',
        'loadavg': '0.81 1.46 1.70 1/765 17958\n'
    }


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


def draw_illu(illu, rst):
    for t in rst['text_lines']:
        d = np.array([t['x0'], t['y0'], t['x1'], t['y1'], t['x2'],
                      t['y2'], t['x3'], t['y3']], dtype='int32')
        d = d.reshape(-1, 2)
        cv2.polylines(illu, [d], isClosed=True, color=(255, 255, 0))
    return illu


def extract_rot(img, save_path=''):
    params = get_predictor(checkpoint_path)(img)
    if len(save_path):
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


def recognize_text_from_posters(img):
    """
    从海报中识别文字
    :param img: numpy.ndarray 海报图片
    :return str 识别到的文字
    """
    # 在图片中寻找文字区域。一个矩形的文字区域由其四个顶点表示。
    box_coordinates = extract_rot(img)
    if len(box_coordinates) == 0:
        return ''

    max_text_height = box_coordinates[0]['text height']
    text = ''
    for i, params in enumerate(box_coordinates):
        # 只识别文字高度在最大文字高度 70% 以内的文字区域
        if params['text height'] < max_text_height * 0.7:
            break
        # 如果文字区域的倾角超过了可容忍的范围
        if np.abs(params['angle']) >= correction_threshold:
            center = (params['x0'], params['y0'])
            # 以 (x0, y0)，即左上角顶点为中心旋转图片
            M = cv2.getRotationMatrix2D(center, params['angle'], 1)
            # 将左上角顶点平移至原点 (x0, y0) -> (0, 0)
            M[0][2] -= center[0]
            M[1][2] -= center[1]
            # 计算文字宽度。认为 (x0, y0) 和 (x1, y1) 之间的距离为文字宽度。
            text_width = int(np.ceil(np.sqrt(
                (params['y1'] - params['y0']) ** 2 + (params['x1'] - params['x0']) ** 2)))
            rot = cv2.warpAffine(img, M, (text_width, params['text height']))
        else:   # 倾角可以容忍，不旋转文字
            left_x = int(min(params['x0'], params['x3']))
            right_x = int(max(params['x1'], params['x2']))
            upper_y = int(min(params['y0'], params['y1']))
            lower_y = int(max(params['y2'], params['y3']))
            rot = img[upper_y:lower_y, left_x:right_x]

        text += image_to_string(rot, config=tesseract_options) + '\n'

    return text


if __name__ == '__main__':
    dataset_path = 'dataset'
    result_path = 'results'
    rot_filename = 'rot.png'
    recognized_text_filename = 'suppressed_text.txt'

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
