# -*- coding: utf-8 -*-

from Tkinter import *

win = Tk()
win.title("Python GUI")    # 添加标题

# 创建一个容器,
monty = LabelFrame(win, text=" Monty Python ")     # 创建一个容器，其父容器为win
monty.grid(column=0, row=0, padx=10, pady=10)       # padx  pady   该容器外围需要留出的空余空间
aLabel = Label(monty, text="A Label")

Label(monty, text="Chooes a number").grid(column=1, row=0)    # 添加一个标签，并将其列设置为1，行设置为0
Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')      # 设置其在界面中出现的位置  column代表列   row 代表行

# button被点击之后会被执行
def clickMe():   # 当acction被点击时,该函数则生效
  action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())     # 设置button显示的内容
  print('check3 is %s %s' % (type(chvarEn.get()), chvarEn.get()))

# 按钮
action = Button(monty, text="Click Me!", command=clickMe)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=2, row=1)    # 设置其在界面中出现的位置  column代表列   row 代表行

# 文本框
name = StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = Entry(monty, width=12, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
nameEntered.grid(column=0, row=1, sticky=W)       # 设置其在界面中出现的位置  column代表列   row 代表行
nameEntered.focus()     # 当程序运行时,光标默认会出现在该文本框中


# 复选框
chVarDis = IntVar()   # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0
check1 = Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled')    # text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态
check1.select()     # 该复选框是否勾选,select为勾选, deselect为不勾选
check1.grid(column=0, row=4, sticky=W)       # sticky=W  当该列中其他行或该行中的其他列的某一个功能拉长这列的宽度或高度时，设定该值可以保证本行保持左对齐，N：北/上对齐  S：南/下对齐  W：西/左对齐  E：东/右对齐

chvarUn = IntVar()
check2 = Checkbutton(monty, text="UnChecked", variable=chvarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=W)

chvarEn = IntVar()
check3 = Checkbutton(monty, text="Enabled", variable=chvarEn)
check3.select()
check3.grid(column=2, row=4, sticky=W)

# 单选按钮

# 定义几个颜色的全局变量
colors = ["Blue", "Gold", "Red"]

# 单选按钮回调函数,就是当单选按钮被点击会执行该函数
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])      # 设置整个界面的背景颜色
        print(radVar.get())
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])

radVar = IntVar()    # 通过IntVar() 获取单选按钮value参数对应的值
radVar.set(99)
for col in range(3):
    # curRad = 'rad' + str(col)
  curRad = Radiobutton(monty, text=colors[col], variable=radVar, value=col, command=radCall)    # 当该单选按钮被点击时，会触发参数command对应的函数
  curRad.grid(column=col, row=5, sticky=W)     # 参数sticky对应的值参考复选框的解释

# 滚动文本框
scrolW = 30 # 设置文本框的长度
scrolH = 3 # 设置文本框的高度


win.mainloop()      # 当调用mainloop()时,窗口才会显示出来