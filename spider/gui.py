#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''网络爬虫图形用户接口'''

from tkinter import *   #Tk模块
import tkinter.scrolledtext
import tkinter.font
import tkinter.messagebox


def close_window(window):
    """关闭窗口时给出提示"""
    if tkinter.messagebox.askyesno("关闭窗口", "真的要退出吗？(是/否)", icon="question"):
        window.destroy() 


class App(Frame):
    """构建窗口程序,使用grid()布局
    """
    def __init__(self, spider, master=None):
        self.master = master
        self.spider = spider                          #网络爬虫类实例化
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        #创建一个标签，设置文字及背景属性
        self.label = Label(text='网络爬虫', font='Helvetica -24 bold', fg='snow', bg='tomato')
        #将标签放置在窗口中的位置
        self.label.grid(row=0, column=0, columnspan=4,sticky=W+E+N+S)

        #创建网址前部文本输入框
        self.label1 = Label(text='网址前部分：', font='Helvetica -15 bold')
        self.label1.grid(row=1, column=0, sticky=E)
        
        self.text1=Entry()
        self.text1.grid(row=1, column=1,columnspan=3, sticky=W)
        self.url_path = StringVar()
        self.url_path.set("")
        self.text1["textvariable"] = self.url_path
        self.text1.config(font="Arial 10 bold", width=60)

        #创建数字文本输入框
        self.label2 = Label(text='起始序号：', font='Helvetica -15 bold')
        self.label2.grid(row=2, column=0,sticky=E)
        
        self.text2=Entry()
        self.text2.grid(row=2, column=1, sticky=W)
        self.start_id = StringVar()
        self.start_id.set("")
        self.text2["textvariable"] = self.start_id
        self.text2.config(font="Arial 10 bold", width=20)

        self.label3 = Label(text='结束序号：', font='Helvetica -15 bold')
        self.label3.grid(row=2, column=2, sticky=E)
        
        self.text3=Entry()
        self.text3.grid(row=2, column=3,sticky=W)
        self.end_id = StringVar()
        self.end_id.set("")
        self.text3["textvariable"] = self.end_id
        self.text3.config(font="Arial 10 bold", width=20)
        
        #创建抓取结果数据文件名称输入框
        self.label4 = Label(text='保存文件名称：', font='Helvetica -15 bold')
        self.label4.grid(row=3, column=0, sticky=E)
        
        self.text4=Entry()
        self.text4.grid(row=3, column=1,columnspan=3, sticky=W)
        self.file_name = StringVar()
        self.file_name.set("")
        self.text4["textvariable"] = self.file_name
        self.text4.config(font="Arial 10 bold", width=60)
        
             
        #创建一个按钮，点击时运行网络爬虫
        self.hi_there = Button(text='点击抓取', 
                                command=lambda : self.spider.catch( str(self.url_path.get()), 
                                                                    int(self.start_id.get()), 
                                                                    int(self.end_id.get()),
                                                                    str(self.file_name.get())))
                                                                    
        self.hi_there.grid(row=4, column=0, sticky=W)

        #创建退出按钮
        self.QUIT = Button(text='  QUIT  ', fg='red', command=lambda : close_window(self.master))
        self.QUIT.grid(row=4, column=3, sticky=E)
