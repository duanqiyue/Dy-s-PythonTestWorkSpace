#coding:utf-8
from Tkinter import *


class TestTK:
    def createTk(self,title):
        tk = Tk()
        tk.title(title)
        frameLeft = LabelFrame(tk,width=400,height=400,bg="#c3c3c3").pack()
        frameRight = LabelFrame(tk, width=400, height=400).pack()
        mainloop()

w1 = TestTK().createTk("测试窗口1")

