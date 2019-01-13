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





def parse_img(url,charlist):
    try:
        content=urllib2.urlopen(url).read()
        soup = BeautifulSoup(content,features="html5lib")
        folder = 'movie_characters'
        if not os.path.exists(folder):  # 如果文件夹不存在则新建
            os.mkdir(folder)
        for item in  soup.find_all('li',{'class':re.compile('celebrity')}):
             actor=item.a['title'].split(' ')[0]
             url=item.a.div['style'][22:-1]
             if actor not in charlist:
                 urllib2.urlretrieve(url,'E:\ee208\crawler\spiders\movie_characters\%s.jpg' % actor)
                 print(actor)
                 charlist.append(actor)
                 file=open('character','a',encoding='utf8')
                 file.write(actor+'\n')
                 file.close()

    except:
        print('There is wrong！')
def parse(url,namelist,charlist):
    content = urllib2.urlopen(url).read()
    content = content.decode(encoding="utf8")
    content = json.loads(content)
    for d in content["data"]:
        name=d['title']
        if name not in namelist:
            url=d['url']
            print(url)
            parse_img(url,charlist)
            namelist.append(name)
            file=open('movie_c','a',encoding='utf8')
            file.write(name+'\n')
            file.close()



def main():
    try:
        url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'
        with open('character', 'r',encoding='utf8') as f1:
            charlist = f1.readlines()
        count=len(charlist)
        for i in range(0, count):
            charlist[i] = charlist[i].strip('\n')
        with open('movie_c', 'r',encoding='utf8') as f2:
            namelist = f2.readlines()
        count=len(namelist)
        for i in range(0, count):
            namelist[i] = namelist[i].strip('\n')
        count=int(count/20)
        while(count<10000):
            url=url[:77]+str(count)
            parse(url,namelist,charlist)
            count+=1
    except:
        time.sleep(3600)
        main()

if __name__ == '__main__':
    main()
