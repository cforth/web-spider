# -*- coding: utf-8 -*-
# Python3.4.1

from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #创建一个标签，设置文字及背景属性
        self.label1 = Label(self, text='Hello World!', font='Helvetica -24 bold', fg='red', bg='blue')
        #将标签放置在窗口中的位置
        self.label1.pack(fill='none', expand=1, ipadx=500, ipady=20, padx=1, pady=1, side='top')

        #创建第二个标签，同上
        self.label2 = Label(self, text='Hello World!', font='Helvetica -12 bold', bg='green')
        self.label2.pack(fill='none', expand=1, ipadx=100, ipady=20, padx=5, pady=5, side='top')

        #创建一个按钮，点击时运行say_hi
        self.hi_there = Button(self)
        self.hi_there['text'] = "Hello World\n(click me)"
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(ipadx=100, ipady=20, padx=5, pady=5, side='top')

        #创建退出按钮
        self.QUIT = Button(self, text='QUIT', fg='red', command=root.destroy)
        self.QUIT.pack(ipadx=120, ipady=20, padx=5, pady=5, side='bottom')

    def say_hi(self):
        print('hi there, everyone!')


root = Tk()
root.title('我的窗口标题')
root.geometry('500x500+200+100')  #窗口大小，位置
root.maxsize(1000, 1000)          #窗口最大尺寸
root.minsize(500, 500)


app = App(master=root)            #初始化窗口
app.mainloop()                    #进入消息循环
