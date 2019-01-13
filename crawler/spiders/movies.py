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





def parse_img(url,name):
    try:
        folder = 'movie_img1'
        if not os.path.exists(folder):  # 如果文件夹不存在则新建
            os.mkdir(folder)
        urllib2.urlretrieve(url,'E:\ee208\crawler\spiders\movie_img1\%s.jpg' % name)
    except:
        print('No image!')

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
                cover=d['cover']
                review='https://movie.douban.com/subject/1292064/reviews'
                review_url=url+review[-7:]
                comments='https://movie.douban.com/subject/1292064/comments'
                comments_url=url+comments[-8:]
                page.append(name)
                page.append(rate)
                page.append(directors)
                page.append(casts)
                page.append(cover)
                page.append(review_url)
                page.append(comments_url)
                parse_page(page)
                file=open('movie','a',encoding='utf8')
                file.write(name+'\n')
                file.close()
                namelist.append(name)
    except:
        print('There is wrong!')
def add_page_to_folder(movie_name,data):  # 将网页存到文件夹里，将网址和对应的文件名写入index.txt中
    folder = 'movie_information1'  # 存放网页的文件夹
    filename =movie_name  # 将网址变成合法的文件名
    if not os.path.exists(folder):  # 如果文件夹不存在则新建
        os.mkdir(folder)
    f = open(os.path.join(folder, filename), 'w',encoding='utf8')
    f.write(data)  # 将网页存入文件
    f.close()


# def parse_reviews(url):
#     content = urllib2.urlopen(url).read()

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
    parse_img(page[4],page[0])
    # d['reviews']=parse_reviews(page[5])
    data['comments']=parse_comments(page[6])
    # data=json.dumps(data)
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
            url=url[:77]+str(count+1000)
            parse(url,namelist)
            count+=1
    except:
        time.sleep(360)


if __name__ == '__main__':
    main()

