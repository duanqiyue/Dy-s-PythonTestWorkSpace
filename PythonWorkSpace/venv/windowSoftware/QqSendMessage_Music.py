#coding:utf-8
import win32gui
import os
import win32con
import win32api
import win32clipboard as w
import time

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
        print "完成！"

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