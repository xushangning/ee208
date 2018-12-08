# -*- coding: utf-8 -*-
import threading
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
import urllib

# q是任务队列
# NUM是并发线程总数
q = Queue.Queue()
NUM = 4
crawled = []
varLock = threading.Lock()
# 具体的处理函数，负责处理单个任务
def get_page(page):
    print('downloading page %s' % page)
    time.sleep(0.5)
    content = ''
    fails = 0
    while True:
        try:
            if fails >= 1:
                break
            req = urllib2.Request(page)
            response = urllib2.urlopen(req, None, 3)
        except:
            fails += 1
        else:
            try:
                if 'text/html;' in response.headers['Content-Type'].split():
                     content = response.read().decode('utf-8')
            except:
                print(page)
            break

    return content

def get_all_links(content, page):
    links = []
    soup = BeautifulSoup(content)
    for i in soup.findAll('a',{'href':re.compile('^http|^/')}):
        url=urlparse.urljoin(page,i['href'])+'\n'
        links.append(url)
    return links
def valid_filename(s):
    import string
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    s = ''.join(c for c in s if c in valid_chars)
    return s
def add_page_to_folder(page, content):  # 将网页存到文件夹里，将网址和对应的文件名写入index.txt中
    index_filename = 'index.txt'  # index.txt中每行是'网址 对应的文件名'
    folder = 'html'  # 存放网页的文件夹
    if(content):
        filename = valid_filename(page)  # 将网址变成合法的文件名
        index = open(index_filename, 'a')
        index.write(page + '\t' + filename + '\n')
        index.close()
        if not os.path.exists(folder):  # 如果文件夹不存在则新建
            os.mkdir(folder)
        f = open(os.path.join(folder, filename), 'w', encoding='utf-8')
        try:
            f.write(content)  # 将网页存入文件
        except UnicodeEncodeError as e:
            raise e
        f.close()

# 这个是工作进程，负责不断从队列取数据并处理
def working():
    global count
    while 1:
        page = q.get()
##        if varLock.acquire():
        if page not in crawled:
##                varLock.release()
##        else:
##                varLock.release()
            count+=1
            content = get_page(page)
            outlinks = get_all_links(content,page)
            add_page_to_folder(page, content)
            for link in outlinks:
                q.put(link)
            if varLock.acquire():
                graph[page] = outlinks
                crawled.append(page)
                varLock.release()
            q.task_done()


count = 0


start = time.clock()
graph = {}
q.put('https://www.zhihu.com/')
for i in range(NUM):
    t = threading.Thread(target=working)
    t.setDaemon(True)
    t.start()
while count<30000:
    pass
end = time.clock()
print(end-start)
