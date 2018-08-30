#coding:utf-8
import sys
import time
import urllib2
import bs4
import os
import pymysql
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('gb18030')

# 获取数据库连接
db = pymysql.connect(host="localhost", user="root",password="ning", db="test", port=3306)
# 获取游标
cur = db.cursor()




def insert_words(wordsList):
    x = 0
    while x<len(wordsList):
        try:
            a = str(wordsList[x])
            cur.execute("INSERT INTO `test`.`words`(`id`, `word`, `first_word`) VALUES (default, '"+a+"', '')")  # 像sql语句传递参数
            # 提交
            db.commit()
            print "成功 : "+str(wordsList[x])
        except Exception as e:
            # 错误回滚
            print str(e)+" : 错误 : "+wordsList[x]
            db.rollback()
        x+=1


mymap=['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']

#函数1，根据关键字获取查询网页
def baidu_search(sound,pagenum):
    url='http://chengyu.t086.com/list/'+str(sound)+'_'+str(pagenum)+'.html'
    html=urllib2.urlopen(url).read()
    return html

 #函数2，处理一个要搜索的关键字
def deal_key():
    wordsList = []
    key_words="成语词典"
    if os.path.exists('data')==False:
        os.mkdir('data')
    filename='data\\'+key_words.decode("utf-8")+'.txt'
    fp=open(filename,'wb')                                                              #打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
    if fp:
        pass
    else:
        print('文件打失败：'+filename)
        return
    x=0
    j=1
    while x<=len(mymap):
        y = 1
        while y<len(mymap):
            try:
                htmlpage = baidu_search(mymap[x], y)
            except BaseException:
                print 'http://chengyu.t086.com/list/'+str(mymap[x])+'_'+str(y)+'.html : 找不到该网址'
            soup = BeautifulSoup(htmlpage)
            for item in soup.findAll("div", {"class": "listw"}):
                ulItem = item.find('ul')
                for liItem in ulItem.findAll("li"):
                    aItem = liItem.find("a")
                    wordsList.append(str(aItem.get_text().encode("utf-8")))
                    if len(wordsList) == 500:
                        insert_words(wordsList)
                        wordsList = []
            y+=1
        x+=1
    fp.close()



#脚本入口
print('Start:')
deal_key()
db.close()
print('End！')