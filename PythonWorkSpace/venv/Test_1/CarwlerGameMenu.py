#-*- coding:utf-8 -*-
import sys
import time
import urllib2
import bs4
import os
import requests
from bs4 import BeautifulSoup


def baidu_search(pagenum):
    url='https://down.gamersky.com/page/pc/0-0-0-0-0-0-0-10_'+pagenum+'.html'
    html=urllib2.urlopen(url).read()
    return html

def deal_key():
    if os.path.exists('data')==False:
        os.mkdir('data')
    if os.path.exists('img')==False:
        os.mkdir('img')
    fileName_text= '排行榜'
    filename='data\\'+fileName_text.decode("utf-8")+'.txt'
    # fp=open(filename,'wb')                                                       #打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
   # if fp:
   #      pass
   #  else:
   #      print('文件打失败：'+filename)
   #      return
    x=1
    page_num = 1;
    while x<=5:
        htmlpage=baidu_search(str(x))
        soup=BeautifulSoup(htmlpage)
        for item in soup.findAll("li", {"class": "lx0"}):                #这个格式应该参考百度网页布局
            img_item  = item.find('div',{"class","img"}).find('a').find('img').get('src')
            meun_text = item.find('div', {"class", "tit"}).find('a')
            if meun_text:
                # fp.write(str(page_num).decode("utf-8"))
                # fp.write(b'\t')
                # fp.write(meun_text.get_text().encode('utf-8'))
                # fp.write(b'\n')

                fileName_text_2 = meun_text.get_text().encode('utf-8')
                #图片
                try:
                   picres_1 = urllib2.urlopen(img_item).read()
                   jpgname = 'img\\' + fileName_text_2.decode("utf-8") + '.jpg'
                   file_img = open(jpgname, 'wb')  # 打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
                   file_img.write(picres_1)
                except Exception as e:
                    print "失败 : "+fileName_text_2
                page_num+=1
        x=x+1
        # fp.write(b'\n')
    # fp.close()
        file_img.close()


def write_img(findAllItem):

    for link in findAllItem:

        picurl = link.get('src')

        picres = requests.get(picurl).content

        file = open(r"C:\images\%s.jpg"%picurl[-9:-4],"wb")

        file.write(picres)

    file.close()


deal_key()