# -*- coding: utf-8 -*-
import threading
import json
import sys
if sys.version > '3':
	import queue as Queue
else:
	import Queue
import time
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import urllib.parse as urlparse
import os
import ssl
import urllib





def parse_video(url,name):
    try:
        content=urllib2.urlopen(url).read()
        soup = BeautifulSoup(content,features="html5lib")
        trailer=soup.find('a',{'class':re.compile('related-pic-video')})
        url=trailer.get('href','')
        # print(url)
        content=urllib2.urlopen(url).read()
        soup = BeautifulSoup(content,features="html5lib")
        video=soup.find('video')
        video_url=video.find('source').get('src','')
    # print(video_url)
        folder = 'movie_video1'
        if not os.path.exists(folder):  # 如果文件夹不存在则新建
            os.mkdir(folder)
        def auto_down(url,name):
            try:
                urllib2.urlretrieve(url,'E:\ee208\crawler\spiders\movie_video1\%s.mp4' % name)
            except urllib.error.ContentTooShortError:
                print('Network conditions is not good.Reloading.')
                # auto_down(url,name)
        auto_down(video_url,name)
    except:
        print('没有预告片！')
def parse(url,namelist):
    content = urllib2.urlopen(url).read()
    content = content.decode(encoding="utf8")
    content = json.loads(content)
    for d in content["data"]:
        name=d['title']
        if name not in namelist:
            print(name)
            url=d['url']
            print(url)
            parse_video(url,name)
            namelist.append(name)
            file=open('movievideo','a',encoding='utf8')
            file.write(name+'\n')
            file.close()



def main():
    try:
        url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'
        with open('movievideo', 'r',encoding='utf8') as f1:
            namelist = f1.readlines()
        count=len(namelist)
        for i in range(0, count):
            namelist[i] = namelist[i].strip('\n')
        count=int(count/20)
        while(count<10000):

            url=url[:77]+str(count+1000)
            parse(url,namelist)
            count+=1
    except:
        time.sleep(3600)
        main()

if __name__ == '__main__':
    main()
