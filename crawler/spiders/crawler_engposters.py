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

def parse_img(url):
    try:
        folder = 'movie_englishposters'
        if not os.path.exists(folder):  # 如果文件夹不存在则新建
            os.mkdir(folder)
        content1 = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content1,features="html5lib")
        con=soup.find('a',{'href':re.compile('^http://www.imdb.com/title/')})
        imdburl=con.get('href','')
        content2 = urllib2.urlopen(imdburl).read()
        soup1 = BeautifulSoup(content2,features="html5lib")
        country=soup1.find('a',{'href':re.compile('^/search/title\?country')}).string
        if country in ['USA','UK']:
            poster=soup1.find('div',{'class':re.compile('poster')})
            img=poster.a.img
            imgurl=img.get('src','')
            title=img.get('title','')[:-7]
            print(img)
            print(title)
            urllib2.urlretrieve(imgurl,'E:\ee208\crawler\spiders\movie_englishposters\%s.jpg' % title)
    except:
        print('There is wrong！')
def parse(url,namelist):
    content = urllib2.urlopen(url).read()
    content = content.decode(encoding="utf8")
    content = json.loads(content)
    for d in content["data"]:
        name=d['title']
        if name not in namelist:
            url=d['url']
            parse_img(url)
            namelist.append(name)
            file=open('movie_p','a',encoding='utf8')
            file.write(name+'\n')
            file.close()


def main():
    try:
        url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'
        with open('movie_p', 'r',encoding='utf8') as f2:
            namelist = f2.readlines()
        count=len(namelist)
        for i in range(0, count):
            namelist[i] = namelist[i].strip('\n')
        count=int(count/20)
        while(count<10000):
            url=url[:77]+str(count)
            parse(url,namelist)
            count+=1
    except:
        time.sleep(3600)
        main()

if __name__ == '__main__':
    main()
