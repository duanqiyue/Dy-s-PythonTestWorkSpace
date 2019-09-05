#coding:utf-8
from Tkinter import *
from tkMessageBox import *
import Tkinter
import time
import thread
import QqSendMessage_Music as qsmm
import WxBot as wxBot


class TestTK:
    message = qsmm.Message()
    wxBot = wxBot.WxBot()

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
        # 文本域
        txtMsgList = Text(montyLeft, width=80,height=40)
        txtMsgList.grid(column=0,row=1)


        # 右边容器
        montyRight = LabelFrame(montyMain,text="微信模块功能")
        montyRight.grid(column=2,row=0,rowspan=3,sticky=Tkinter.N+Tkinter.S)
        # 启动事件
        def startWXBot():
            self.startWXBot()
        #启动按钮
        Button(montyRight, text="启动微信功能（需扫码）", command=startWXBot, width=40).grid(column=0, row=0, columnspan=3, pady=15)
        # 微信发送事件
        def sendWxMessage():
            self.sendWxMessage(name.get(),txtMsgList.get("0.0", "end"))
        # 微信发送按钮
        Button(montyRight, text="微信发送消息", command=sendWxMessage, width=40).grid(column=0, row=1, columnspan=3)


        # 中间容器
        montyCenter = LabelFrame(montyMain, text="设置发送的人（备注）") # 创建一个容器，其父容器为tk
        montyCenter.grid(column=1,row=0,sticky=Tkinter.N + Tkinter.S)  # padx  pady   该容器外围需要留出的空余空间
        # 文本框
        name = StringVar()  # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
        nameEntered = Entry(montyCenter, width=40,textvariable=name)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
        nameEntered.grid(column=0,row=0,columnspan=3)  # 设置其在界面中出现的位置  column代表列   row 代表行
        nameEntered.focus()  # 当程序运行时,光标默认会出现在该文本框中
        # 开始事件
        def ClickMeForSend():
            self.ClickMeForSend(txtMsgList.get("0.0", "end"),name.get())
        # 开始按钮
        action = Button(montyCenter,text="开始", command=ClickMeForSend,width=7)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
        action.grid(column=1,columnspan = 2,row=1,padx = 5 ,pady=10,sticky=N)
        # 暂停事件
        def ClickMeForSuspend():
            self.ClickMeForSuspend()
        # 暂停按钮
        ca = Button(montyCenter, text="停止", command=ClickMeForSuspend, width=7)
        ca.grid(column=2, row=1,pady=10,sticky=N)
        # 歌曲提示
        Label(montyCenter,text="输入歌曲名查找歌词").grid(column=0, row=2,columnspan=3,sticky="W")
        # 歌曲文本框
        musicName = StringVar()
        musicNameEntry = Entry(montyCenter,width=30,textvariable=musicName)
        musicNameEntry.grid(column=0,row=3,columnspan=2)
        # 查找歌词事件
        def SearchMusic():
            txtMsgList.delete(1.0, Tkinter.END)
            txtMsgList.insert('insert', self.ClickMeForSearchMusic(musicName.get()))
        # 查找歌词按钮
        Button(montyCenter,text="查找",command=SearchMusic,width=7).grid(column=2,row=3,pady=15)

        # 土味情话事件
        def SearchLover():
            txtMsgList.delete(1.0, Tkinter.END)
            txtMsgList.insert('insert',self.ClickMeForSearchLoveWrod())
        # 土味情话提示
        Label(montyCenter, text="数据来自http://www.gexings.com").grid(column=0, row=4, columnspan=4, sticky="W")
        # 查找歌词按钮
        Button(montyCenter, text="一键生成土味情话", command=SearchLover,width=40).grid(column=0, row=5,columnspan=3,pady=15)

        # 投稿提示
        Label(montyCenter, text="同时也希望您提出意见给我们:").grid(column=0, row=6, columnspan=4, sticky="W")
        Label(montyCenter, text="或者也可以写出土味情话给我们:").grid(column=0, row=7, columnspan=4, sticky="W")
        # 投稿文本框
        LoverEmailTextEntry = Text(montyCenter, width=40, height=15)
        LoverEmailTextEntry.grid(column=0, row=8,columnspan=3)

        # 点击投稿事件
        def sendLover():
            if len(LoverEmailTextEntry.get("0.0", "end").replace("\n",""))==0:
                showinfo('提示', '请填入些许内容')
            else :
                self.ClickMeToEmailWithLoverWords(LoverEmailTextEntry.get("0.0", "end"))
                LoverEmailTextEntry.delete(1.0, Tkinter.END)
                showinfo('成功', '感谢您的投稿（建议）我们会认真参考的！')

        # 查找歌词按钮
        Button(montyCenter, text="投稿", command=sendLover, width=40).grid(column=0, row=9, columnspan=3,pady=5)

        Label(tk, text="Producer：STR-DY").grid(column=0, columnspan=2, row=1, sticky=E)
        Label(tk, text="Contact us by QQ：812380163").grid(column=0, columnspan=2, row=2, sticky=E)
        mainloop()


    # 点击方法：启动BOT
    def startWXBot(self):
        thread.start_new_thread(self.wxBot.startWXBot,())

    # 点击方法：发送微信消息
    def sendWxMessage(self,a,b):
        thread.start_new_thread(self.wxBot.sendMssage,(a,b))

    # 发送投稿邮件
    def ClickMeToEmailWithLoverWords(self,loverWords):
        self.message.sendEamil(loverWords)


    # 点击方法：开始
    def ClickMeForSend(self,a,b):
        thread.start_new_thread(self.message.send,(a,b))

    # 点击方法：暂停
    def ClickMeForSuspend(self):
        thread.start_new_thread(self.message.suspend, ("","",""))

    def ClickMeForSearchMusic(self,musicNameText):
        key_words = musicNameText.encode("utf-8") + "歌词"
        return self.message.searchMusicText(key_words)

    def ClickMeForSearchLoveWrod(self):
        str = ""
        url_maps = ["http://www.gexings.com/aiqing/63688.html",
               "http://www.gexings.com/aiqing/63689.html",
               "http://www.gexings.com/aiqing/63687.html",
               "http://www.gexings.com/aiqing/63574.html",
               "http://www.gexings.com/aiqing/63573.html",
               "http://www.gexings.com/aiqing/63571.html",
               "http://www.gexings.com/aiqing/63572.html",
               "http://www.gexings.com/aiqing/63567.html",
               "http://www.gexings.com/aiqing/63569.html",
               "http://www.gexings.com/aiqing/63570.html",
               "http://www.gexings.com/aiqing/63522.html",]
        for url_item in url_maps:
            str += self.message.searchLoveWrod(url_item)
        return str


