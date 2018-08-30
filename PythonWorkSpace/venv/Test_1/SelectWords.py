#coding:utf-8
import pymysql
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('gb18030')

#获取连接
db = pymysql.connect(host="localhost", user="root",password="ning", db="test", port=3306)
#获取游标
cur = db.cursor()

def select_word(word):
    cur.execute("select * from words where first_word = right('"+word.decode("utf-8")+"',1)")
    # 使用 execute()  方法执行 SQL 查询
    data = cur.fetchone()
    return data[1]
