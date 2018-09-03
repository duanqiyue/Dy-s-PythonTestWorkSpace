#coding:utf-8
from Tkinter import *
import time
import QqSendMessage_Music as qsm


class TestTK:
    def createTk(self,title):
        tk = Tk()
        tk.title(title)
        #tk.geometry('350x150')  初始大小
        tk.iconbitmap('logo.ico')
        # 创建一个容器,
        montyMain = LabelFrame(tk, text="")  # 创建一个容器，其父容器为tk
        montyMain.grid(padx=10, pady=10)  # padx  pady   该容器外围需要留出的空余空间
        # 左容器
        montyLeft = LabelFrame(montyMain, text="请输入要发送的内容，一行为一条信息")  # 创建一个容器，其父容器为tk
        montyLeft.grid(column=0,row=0)  # padx  pady   该容器外围需要留出的空余空间
        txtMsgList = Text(montyLeft, width=50,height=40)
        txtMsgList.grid(column=0,row=1)
        # 右容器
        montyRight = LabelFrame(montyMain, text="设置发送的人（备注）") # 创建一个容器，其父容器为tk
        montyRight.grid(column=1,row=0,sticky="n")  # padx  pady   该容器外围需要留出的空余空间
        # 文本框
        name = StringVar()  # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
        nameEntered = Entry(montyRight, width=30,textvariable=name)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
        nameEntered.grid(column=0,row=0,columnspan=2)  # 设置其在界面中出现的位置  column代表列   row 代表行
        nameEntered.focus()  # 当程序运行时,光标默认会出现在该文本框中
        # 点击方法
        sendFlag = True
        def clickMe():
            text_str = txtMsgList.get("0.0", "end")
            name_str = name.get()
            for text_str_line in text_str.split('\n'):
                time.sleep(0.3)
                if sendFlag:
                    qsm.sendMessageBy770(text_str_line, name_str)
                else:
                    break
            print "完成！"

        # 按钮
        action = Button(montyRight,text="开始",command=clickMe,width=7,height=3)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        action.grid(column=0,row=1,pady=30,sticky=S)  # 设置其在界面中出现的位置  column代表列   row 代表行

        ca = Button(montyRight, text="暂停", command=suspend, width=7,height=3)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        ca.grid(column=1, row=1,pady=30,sticky=S)  # 设置其在界面中出现的位置  column代表列   row 代表行
        Label(text="制作人：STR-ddddddddddddddddddy").grid()
        mainloop()