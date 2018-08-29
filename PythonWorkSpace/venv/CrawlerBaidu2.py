#coding:utf-8
import sys
import time
import urllib2
import bs4
import os
from bs4 import BeautifulSoup
mymap=['0','1','2','3','4','5','6','7']

#函数1，根据关键字获取查询网页
def baidu_search(key_words):
    html=urllib2.urlopen(key_words).read()
    return html

#函数3，读取搜索文件内容，依次取出要搜索的关键字
def search_file():
    fp=open('searchfile.txt')
    i=0
    keyword=fp.readline()
    while keyword:
        nPos=keyword.find('\n')
        if nPos>-1:
            keyword=keyword[:-1]#keyword.replace('\n','')
        baidu_search(keyword)
        keyword=fp.readline()

#脚本入口
print('Start:')
search_file()
print('End！')