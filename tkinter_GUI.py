# -*- coding: utf-8 -*-
# Python3.4.1

import tkinter as tk

def resize(ev = None):
    """scale的回调函数
    修改labelDisplay的字体大小，当然其他信息也可以改，比如text
    """
    labelDisplay.config(font = 'Helvetica -%d bold' % scale.get())


root = tk.Tk()
root.title('窗口标题')                #窗口标题
root.geometry("250x150+0+0")         #窗口宽度与高度，位置

#创建一个Label，是要放置在root内的，文本为'Hello World!'，还有字体与背景色  
labelDisplay=tk.Label(root, text='Hello World!', font='Helvetica -12 bold',bg='red')

#将labelDisplay放置进root，如果没有这句话，则不会显示这个组件。fill, expand, ipadx, ipady的说明在下面 
labelDisplay.pack(fill=None, expand=1, ipadx=5, ipady=5)
