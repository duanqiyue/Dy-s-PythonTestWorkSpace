#coding:utf-8
import sys
import time
import urllib2
import bs4
import os
from bs4 import BeautifulSoup
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('gb18030')

#获取连接
db = pymysql.connect(host="localhost", user="root",password="ning", db="test", port=3306)
#获取游标
cur = db.cursor()

def baidu_search(key_word):
    url='http://www.baidu.com/s?wd='+key_word
    html = urllib2.urlopen(url).read()
    return html

def select_word():
    word_list = []
    cur.execute("select * from words")
    # 使用 execute()  方法执行 SQL 查询
    data = cur.fetchall()
    for row in data:
        word_list.append(row[2])
    return word_list

def select_word_id():
    id_list = []
    cur.execute("select * from words")
    # 使用 execute()  方法执行 SQL 查询
    data = cur.fetchall()
    for row in data:
        id_list.append(row[0])
    return id_list

def update_words(first_py_str,id):
    try:
        cur.execute("update words set first_py = '"+first_py_str+"' where id = "+id)  # 像sql语句传递参数
        # 提交
        db.commit()
        print "成功 : " + str(first_py_str)
    except Exception as e:
        # 错误回滚
        print str(e) + " : 错误 : " + id
        db.rollback()


select_word_ids = select_word_id()
x = 0
for item in select_word():
    first_word = str(item).decode("utf-8")
    html_page = baidu_search(first_word)
    soup = BeautifulSoup(html_page)
    span = soup.find("span",{"class","op_exactqa_word_word_pronounce"})
    first_py = span.find("span")
    first_py_str = first_py.get_text()
    print first_py_str
    # id = select_word_ids[x]
    # id_str = str(id)
    # first_py_str_str = str(first_py_str)
    # update_words(first_py_str,id_str)
    # x+=1



