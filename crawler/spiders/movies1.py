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

def parse(url,namelist):
    try:
        content = urllib2.urlopen(url).read()
        content = content.decode(encoding="utf8")
        content = json.loads(content)
        for d in content["data"]:
            page=[]
            name=d['title']
            if name not in namelist:
                print(name)
                directors=d['directors']
                rate=d['rate']
                url=d['url']
                casts=d['casts']
                comments='https://movie.douban.com/subject/1292064/comments'
                comments_url=url+comments[-8:]
                page.append(name)
                page.append(rate)
                page.append(directors)
                page.append(casts)
                page.append(url)
                page.append(comments_url)
                parse_page(page)
                file=open('movie','a',encoding='utf8')
                file.write(name+'\n')
                file.close()
                namelist.append(name)
    except:
        print('There is 404!')

def add_page_to_folder(movie_name,data):  # 将网页存到文件夹里，将网址和对应的文件名写入index.txt中
    folder = 'movie_information'  # 存放网页的文件夹
    filename =movie_name  # 将网址变成合法的文件名
    if not os.path.exists(folder):  # 如果文件夹不存在则新建
        os.mkdir(folder)
    f = open(os.path.join(folder, filename), 'w',encoding='utf8')
    f.write(data)  # 将网页存入文件
    f.close()

def parse_name(url):
    content1 = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content1,features="html5lib")
    con=soup.find('a',{'href':re.compile('^http://www.imdb.com/title/')})
    imdburl=con.get('href','')
    content2 = urllib2.urlopen(imdburl).read()
    soup1 = BeautifulSoup(content2,features="html5lib")
    h1=soup1.find('h1').text
    h1=h1.split("(")[0]
    h1=h1.strip()
    print(h1)
    return h1

def parse_comments(url):
    time.sleep(1.0)
    try:
        content = urllib2.urlopen(url).read()
        count=0
        soup = BeautifulSoup(content,features="html5lib")
        com={}
        for item in  soup.find_all('div',{'class':re.compile('comment-item')}):
            count+=1
            if count>5:
                break
            author=item.find('div',{'class':re.compile('avatar')})
            author=author.a['title']
            comment=item.find('span',{'class':re.compile('short')})
            comment=comment.string
            com[author]=comment
        return com
    except:
        print('No comment!')

def parse_page(page):
    data={}
    data['name']=page[0]
    data['rate']=page[1]
    data['directors']=page[2]
    data['casts']=page[3]
    data['comments']=parse_comments(page[5])
    data['Englishname']=parse_name(page[4])
    data['comments']=parse_comments(page[5])
    print(data)
    add_page_to_folder(page[0],str(data))

def main():
    try:
        url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0'
        with open('movie', 'r',encoding='utf8') as f1:
            namelist = f1.readlines()
        count=len(namelist)
        for i in range(0, count):
            namelist[i] = namelist[i].strip('\n')
        count=int(count/20)+1
        while(count<10000):
            url=url[:77]+str(count)
            parse(url,namelist)
            count+=1
    except:
        time.sleep(360)


if __name__ == '__main__':
    main()






