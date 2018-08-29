#coding:utf-8
import win32gui
import os
import win32con
import win32api
import win32clipboard as w
import time

def sendMessageBy770(text,winName):
    #设置剪贴板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, str(text).decode("utf-8"))
    w.CloseClipboard()
    win = win32gui.FindWindow(None, u''+str(winName).decode("utf-8"))
    if str(win)=="0":
        return
    # 将剪贴板消息到窗体
    win32gui.SendMessage(win, 770, 0, 0)
    # # 模拟按下回车键
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)  # 键盘按下  68  D
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开  D 68


def sendMusic(winName):
    fp = open('music.txt')
    text_str = "text"
    i = 0
    keyword = fp.readline()
    while keyword:
        nPos = keyword.find('\n')
        if nPos > -1:
            keyword = keyword[:-1]  # keyword.replace('\n','')
        text_str = keyword
        sendMessageBy770(text_str, winName)
        keyword = fp.readline()
        time.sleep(0.3)
    fp.close()

