# -*- coding: utf-8 -*-
# Python3.4.1

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title('我的窗口标题')
root.geometry('300x200+0+0')  #窗口大小，位置

#创建一个Label，是要放置在root内的，文本为'Hello World!'，还有字体与背景色  
labelDisplay=tk.Label(root, text='Hello World!', font='Helvetica -12 bold', bg='red')
#将labelDisplay放置进root，如果没有这句话，则不会显示这个组件。
labelDisplay.pack(fill= 'none', expand=1, ipadx=5, ipady=5)

labelDisplay1=tk.Label(root, text='Hello World!', font='Helvetica -12 bold', bg='green')  
labelDisplay1.pack(fill='both', expand=1, padx=5, pady=5) 

app = Application(master=root)
app.mainloop()
