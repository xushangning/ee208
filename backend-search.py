from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost:9200'])

"""mapping = {'Movie':{                索引
    'properties':{
        'name':{
            'type':'keyword',
        }
    }
}}
es.indices.create(index='homework1')


import os
path1 = "movie/movie_information"
path2 = "movie/movie_img"
files1 = os.listdir(path1)
files2 = os.listdir(path2)
files1.sort()
files2.sort()
count = 0
f = 0
for p1 in files1[:-1]:
    P1 = os.path.basename(p1)
    P2 = os.path.basename(files2[count])
    count += 1
    if (P1 != P2[:-4] and f == 0):
        P2 = os.path.basename(files2[count])
        count += 1
    if P1 == '.DS_Store':
        continue
    f1 = 'movie/movie_information/'+P1
    f2 = 'movie/movie_img/'+P2
    F1 = open(f1,'rb')
    text = eval(F1.read())
    if text['comments'] is None or len(text['comments']) != 5:
        continue

    movie = {
            'name':text['name'],
            'rate':text['rate'],
            'casts':text['casts'],
            'directors':text['directors'],
            'post':f2,
            str(text['time']):text['script']
        }
    es.index(index='homework1',doc_type='Movie',body=movie)
    print(movie['name'])"""


from flask import Flask              #搜索
from flask import request
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from run_demo_server import recognize_text_from_posters

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/')
def home():
    dsl = {'query':{'match':{'name':'X战警'}}}
    result = es.search(index='homework1',doc_type='Movie',body=dsl)
    res = []
    for i in result['hits']['hits']:
        res.append(i['_source'])
    return res
=======
>>>>>>> dd7243895084e750c9ccaa52cb11233a218fb4a6

@app.route('/results',methods=['GET'])
def text_Search():
    search = request.args.get('name')
    dsl1 = {'query':{'match':{'name':str(search)}}}
    result = es.search(index='homework1',doc_type='Movie',body=dsl1)
<<<<<<< HEAD
    res = []
    for i in result['hits']['hits']:
        res.append(i['_source'])
    return res

@app.route('/result0',methods=['GET'])
def result0():
        search = request.args.get('name')
        dsl2 = {'query':{'term':{'name':str(search)}}}
        result = es.search(index='homework2',doc_type='Movie',body=dsl2)
        res = result['hits']['hits'][0]['_source']
        return res

@app.route('/result1',methods=['POST'])
def result1():
        search = request.files['file']
        search.save('/result1/upload' + secure_filename(search.filename))
        img = cv2.imread('/result1/upload' + secure_filename(search.filename))
        img1 = np.array(img)
        search = recognize_text_from_posters(img1)
        dsl3 = {'query':{'match':{'name':str(search)}}}
        result = es.search(index='homework1',doc_type='Movie',body=dsl3)
        res = result['hits']['hits'][0]['_source']
        return res

@app.route('/result2',methods=['POST'])
def result1():
    search = request.files['file']
    search.save('/result2/upload' + secure_filename(search.filename))
    img = cv2.imread('/result2/upload' + secure_filename(search.filename))
    img1 = np.array(img)
    search = recognize_text_from_posters(img1)
    dsl4 = {'query':{'match':{'time':str(search)}}}
    result = es.search(index='homework1',doc_type='Movie',body=dsl4)
    res = result['hits']['hits'][0]['_source']
    return res

=======
    results = []
    for i in result['hits']['hits']:
        results.append(i['_source'])
    return results

@app.route('/result',methods=['POST','GET'])
def img_Search():
    if request.method == 'GET':
        search = request.args.get('name')
        dsl2 = {'query':{'term':{'name':str(search)}}}
        result = es.search(index='homework2',doc_type='Movie',body=dsl2)
        result1 = result['hits']['hits'][0]['_source']
        return result1

    if request.method == 'POST':
        search = request.files['file']
        search.save('/result/upload' + secure_filename(search.filename))
        img = cv2.imread('/result/upload' + secure_filename(search.filename))
        img1 = np.array(img)
        search = recognize_text_from_posters(img1)
        dsl3 = {'query':{'match':{'time':str(search)}}}
        result = es.search(index='homework1',doc_type='Movie',body=dsl3)
        result2 = result['hits']['hits'][0]['_source']
        return result2
>>>>>>> dd7243895084e750c9ccaa52cb11233a218fb4a6



if __name__ == '__main__':
    app.run()


