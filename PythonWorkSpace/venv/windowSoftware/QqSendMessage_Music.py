#coding:utf-8
import win32gui
import os
import win32con
import win32api
import win32clipboard as w
import time
import sys
import urllib2
import bs4
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Message:
    sendFlag = True

    def suspend(self,a,b,c):
        self.sendFlag = False

    def send(self,a,b):
        if self.sendFlag == False:
            self.sendFlag = True
        text_str = a
        name_str = b
        for text_str_line in text_str.split('\n'):
            time.sleep(0.3)
            if self.sendFlag:
                self.sendMessageBy770(text_str_line, name_str)
            else:
                break
        print "Over!"

    def sendMessageBy770(self,text,winName):
        #设置剪贴板
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, text)
        w.CloseClipboard()
        win = win32gui.FindWindow(None, u''+winName)
        if str(win)=="0":
            return
        # 将剪贴板消息到窗体
        win32gui.SendMessage(win, 770, 0, 0)
        # # 模拟按下回车键
        win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)  # 键盘按下  68  D
        win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开  D 68

    def searchMusicText(self,key_words):
        url = 'http://www.baidu.com/s?wd=' + key_words + '&pn=1'
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        str = ""
        for item in soup.findAll("p", {"class": "wa-musicsong-lyric-line"}):  # 这个格式应该参考百度网页布局
            str += item.get_text().encode('utf-8')

        return str

    def searchLoveWrod(self,url):
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        str = ""
        div = soup.find("div", {"class": "content"})
        for item in div.findAll("p"):
            item_text = item.get_text()
            if len(item_text)!=0:
                item_text_start = item_text[0:1].encode('utf-8')
                item_text_start_2 = item_text[1:2].encode('utf-8')
                if item_text_start_2=="1"or item_text_start_2=="2" or item_text_start_2=="3" or item_text_start_2=="4" or item_text_start_2=="5" or item_text_start_2=="6" or item_text_start_2=="7" or item_text_start_2=="8" or item_text_start_2=="9":
                    str += item_text[3:len(item_text)].encode('utf-8') + "\r\n"
                elif item_text_start=="1"or item_text_start=="2" or item_text_start=="3" or item_text_start=="4" or item_text_start=="5" or item_text_start=="6" or item_text_start=="7" or item_text_start=="8" or item_text_start=="9":
                    str += item_text[2:len(item_text)].encode('utf-8') + "\r\n"
                else :
                    str += item_text[0:len(item_text)].encode('utf-8') + "\r\n"

        return str


    def getIp(self):
        url = 'http://www.baidu.com/s?wd=ip&pn=1'
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        item = soup.find("div", {"class": "c-span21 c-span-last op-ip-detail"})
        str_addresss = item.get_text().encode('utf-8')

        sender = 'duanqiyue666@163.com'
        receiver = '812380163@qq.com'
        subject = '沙雕发消息有人登陆了！'
        username = 'duanqiyue666@163.com'
        password = 'ai812380163'

        msg = MIMEText(str_addresss, 'plain', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = '段奇越<duanqiyue666@163.com>'
        msg['To'] = receiver
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()



    def sendEamil(self,loverWordsToEmail):
        sender = 'duanqiyue666@163.com'
        receiver = '812380163@qq.com'
        subject = '土味情话投稿'
        username = 'duanqiyue666@163.com'
        password = 'ai812380163'

        msg = MIMEText(loverWordsToEmail, 'plain', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = '段奇越<duanqiyue666@163.com>'
        msg['To'] = receiver
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print "成功"



    # def searchPoetryText(self,key_words):
    #     url = 'https://so.gushiwen.org/search.aspx?value='+key_words
    #     html = urllib2.urlopen(url).read()
    #     soup = BeautifulSoup(html)
    #     str = ""
    #     print str


