#coding:utf-8
from Tkinter import *

def main():
    root = Tk()
    txtMsgList = Text(root,width=200)
    txtMsgList.pack(side=LEFT)
    canvas.pack()
    canvas.create_text(200, 40, text="测试弹出框", fill="black", font=("微软雅黑", 16))
    canvas.create_image(10, 70, anchor=NW, image=PhotoImage(file="1.gif"))

    def moverectangle(event):
        if event.keysym == "Up":
            canvas.move(3, 0, -5)
        elif event.keysym == "Down":
            canvas.move(3, 0, 5)
        elif event.keysym == "Left":
            canvas.move(3, -5, 0)
        elif event.keysym == "Right":
            canvas.move(3, 5, 0)
        else:
            canvas.move(3, 5, 5)

    canvas.create_rectangle(200, 200, 220, 220, fill="red")
    # 让tkinter监视KeyPress事件，当该事件发生时调用moverectangle函数
    # bind_all第2个参数是回调函数，不能接收参数传递，所以在函数内部建立回调函数
    canvas.bind_all("<KeyPress-Up>", moverectangle)
    canvas.bind_all("<KeyPress-Down>", moverectangle)
    canvas.bind_all("<KeyPress-Left>", moverectangle)
    canvas.bind_all("<KeyPress-Right>", moverectangle)
    canvas.bind_all("<KeyPress-Return>", moverectangle)

    mainloop()

main()