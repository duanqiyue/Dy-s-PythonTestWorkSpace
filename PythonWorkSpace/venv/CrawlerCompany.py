#coding:utf-8
import sys
import time
import urllib2
import bs4
import os
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
mymap=['0','1','2','3','4','5','6','7']

#函数1，根据关键字获取查询网页
def baidu_search():
    url='http://www.fortunechina.com/fortune500/c/2018-07/19/content_311046.htm'
    html=urllib2.urlopen(url).read()
    return html

 #函数2，处理一个要搜索的关键字
def deal_key():
    if os.path.exists('data')==False:
        os.mkdir('data')
    filename='data\\111.txt'
    fp=open(filename,'w')                                                              #打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
    if fp:
        pass
    else:
        print('文件打失败：'+filename)
        return
    x=0
    while x<1:
        htmlpage=baidu_search()
        soup=BeautifulSoup(htmlpage)
        for item in soup.findAll("table", {"id": "yytable"}):
            # tr = item.find('thead')
            # fp.write(tr.get_text().encode("utf-8").replace("\n","\t"))
            # fp.write(b'\n')

            for bodyTr in item.find("tbody").findAll("tr"):
                tdList = bodyTr.findAll("td")
                inCome = ""
                if(tdList[4].get_text().encode("utf-8").replace(",","")=="-"):
                    inCome="0"
                else:
                    inCome=tdList[4].get_text().encode("utf-8").replace(",","")
                stringInsert = "INSERT INTO `test`.`company`(`id`, `rank`, `ly_rank`, `name`, `income`, `profit`, `country`) VALUES (default, "+tdList[0].get_text().encode("utf-8")+", "+tdList[1].get_text().encode("utf-8").replace("--","0")+", '"+tdList[2].get_text().encode("utf-8").replace("'","")+"', "+tdList[3].get_text().encode("utf-8").replace(",","")+", "+inCome+", '"+tdList[5].get_text().encode("utf-8")+"');"
                fp.write(stringInsert.decode("utf-8"))
                fp.write(b'\n')
        x=x+1
    fp.close()


#脚本入口
print('Start:')
deal_key()
print('End！')