# -*- coding: utf-8 -*-
#网络爬虫0.6版
# Python3.4.1

from tkinter import *   #Tk模块
from tkinter.scrolledtext import *
import urllib.request   #网络模块
import re               #正则表达式模块
import codecs           #文件编码转换
import sys
import tkinter.font
import tkinter.messagebox

###############################################################
#窗口模块开始

def close_window(window):
    """关闭窗口时给出提示"""
    if tkinter.messagebox.askyesno("关闭窗口", "真的要退出吗？(是/否)", icon="question"):
        window.destroy() 


class App(Frame):
    """构建窗口程序
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #创建一个标签，设置文字及背景属性
        self.label = Label(self, text='网络爬虫（股票抓取）', font='Helvetica -24 bold', fg='snow', bg='tomato')
        #将标签放置在窗口中的位置
        self.label.pack(fill='none', expand=1, ipadx=500, ipady=20, padx=1, pady=1, side='top')

        #创建网址前部文本输入框
        self.label1 = Label(text='输入网页抓取网址前部分：', font='Helvetica -15 bold')
        self.label1.pack(fill='none', expand=1, ipadx=400,side='top')
        self.text1=Entry()
        self.text1.pack(fill='none', expand=1, ipadx=100, ipady=5, padx=5, pady=5, side='top')
        self.contents = StringVar()
        self.contents.set("")
        self.text1["textvariable"] = self.contents
        self.text1.config(font="Arial 10 bold")

        #创建数字文本输入框
        self.label2 = Label(text='输入起始序号：', font='Helvetica -15 bold')
        self.label2.pack(fill='none', expand=1, ipadx=400,side='top')
        self.text2=Entry()
        self.text2.pack(fill='none', expand=1, ipadx=100, ipady=5, padx=5, pady=5, side='top')
        self.contents2 = StringVar()
        self.contents2.set("")
        self.text2["textvariable"] = self.contents2
        self.text2.config(font="Arial 10 bold")

        self.label3 = Label(text='输入结束序号：', font='Helvetica -15 bold')
        self.label3.pack(fill='none', expand=1, ipadx=400,side='top')
        self.text3=Entry()
        self.text3.pack(fill='none', expand=1, ipadx=100, ipady=5, padx=5, pady=5, side='top')
        self.contents3 = StringVar()
        self.contents3.set("")
        self.text3["textvariable"] = self.contents3
        self.text3.config(font="Arial 10 bold")

        #创建执行结果输出文本框
        self.textout= ScrolledText(wrap = WORD,height=10)
        self.textout.pack(fill='none', expand=1, padx=5, pady=5, side='top')
             
        #创建一个按钮，点击时运行网络爬虫
        self.hi_there = Button()
        self.hi_there['text'] = "点击股票抓取"
        self.hi_there['command'] = self.do_stock
        self.hi_there.pack(ipadx=50, ipady=10, padx=20, pady=10, side='left')

        #创建退出按钮
        self.QUIT = Button(text='QUIT', fg='red', command=lambda : close_window(root))
        self.QUIT.pack(ipadx=60, ipady=10, padx=20, pady=10, side='right')

    def do_stock(self):
        
        #运行网络爬虫
        spider_go(str(self.contents.get()), str(self.contents2.get()), str(self.contents3.get()))

        #可选，删除之前已获取股票数据中的重复行
        remove_r('new.txt','old.txt','save.txt')

        #可选，功能测试，在窗口中显示爬虫抓取后并去重的数据
        with open('f:/temp/save.txt', 'r') as f:
            textoutstr = str(f.read())

        self.textout.insert(INSERT, textoutstr)

#窗口模块结束

##############################################################
##网络爬虫模块开始
    
def get_stock_info(url):
    """抓取网页，利用正则表达式匹配股票信息。
    网页请求头部为Chrome信息，网页编码为gb2312。
    若网页中股票代码存在，返回股票信息。
    """
    user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.6 Safari/537.36'
    req = urllib.request.Request(url)
    req.add_header('User-Agent', user_agent)

    response = urllib.request.urlopen(req)  #抓取网页      
    text = response.read().decode('gb2312', 'ignore')
    
    stock_id = re.findall(r'\d+\.S[ZH]', str(text))                                             #正则匹配股票代码
    price_inid = re.findall(r'<span id="ctl04_lbSpj">(\d+\.\d+)</span>', str(text))             #正则匹配初始价
    price_target = re.findall(r'<span id="ctl04_txTgtPrice">(\d+\.\d+)</span>', str(text))      #正则匹配目标价
    grade = re.findall(r'<span id="ctl04_bgpj">([\u4e00-\u9fa5]+)</span>', str(text))           #正则匹配评级
    trade = re.findall(r'<span id="ctl04_lbHylbmc">([\u4e00-\u9fa5]+)</span>', str(text))       #正则匹配行业
    trade = trade if len(trade) != 0 else '无'
    stock_date = re.findall(r'<span id="ctl04_lblzhxgrq" style="display:inline-block;width:90%;">(\d+\-\d+\-\d+)</span>', str(text))   #正则匹配日期
    
    if len(stock_id) != 0:
        name = stock_id[0]
        sname = '1' + name[0:6] if name[-1] == 'Z' else '0' + name[0:6]
        return '  ["{0}", "{1}", "{2}", "{3}",  "{4}", "{5}"],\n'.format(sname, trade[0], stock_date[0], price_inid[0], price_target[0], grade[0])
    else:
        return ''

def write_stock_file(mystr, file_name):
    """以写入方式打开文件，写入字符串mystr并自动关闭文件。
    """
    with open(file_name, 'a') as f:
        f.write(str(mystr))


def spider_go(url_head, start, end):
    """设置网页抓取地址头部、页面ID范围。
    合成需要抓取的网页地址，在ID范围内循环抓取数据存储在mystr中。
    最后写入文件。
    工作目录为'F:/temp/'。
    """   
    try:
        start_id = int(start)
        end_id = int(end)
    except:
        print('序号输入有误！终止任务！必须输入数字！')
        return

    if end_id < start_id:
        print('序号输入有误！终止任务！起始序号必须小于或等于结束序号！')
        return
        
    file_name = 'f:/temp/new.txt'
    mystr = ''
    task_id = 1
    task_all = end_id - start_id + 1
    
    for i in range(end_id, start_id - 1, -1):
        try:
            mystr = get_stock_info(url_head + str(i))
        except:
            print('网页获取失败！终止任务！错误信息：{0}'.format(sys.exc_info()[0]))
            return
        write_stock_file(mystr, file_name)
        print('任务进度 ({0}/{1})'.format(task_id, task_all))
        task_id = task_id + 1

    print('任务结束，数据存入文件： {0} \n'.format(file_name))
        

def remove_r(file_new, file_old, file_save):
    """从file_new文件中去除file_old中的重复行，并将结果保存在file_save文件中。
    注意文件读取时的编码转换,工作目录为'F:/temp/'。
    """
    file_dir = 'f:/temp/'
    file_new = file_dir + file_new
    file_old = file_dir + file_old
    file_save = file_dir + file_save

    with codecs.open(file_old, 'r', 'utf-8') as f_o:
        stock_id = re.findall(r'\["(\d+)"', str(f_o.read()))

    with codecs.open(file_new, 'r', 'cp936') as f_n:
        for line in f_n:
            stock_id_new = re.findall(r'\["(\d+)"', str(line))
            if stock_id_new[0] not in stock_id:
                write_stock_file(line, file_save)
            else:
                print('{0}行重复，已去除!\n'.format(stock_id_new[0]))

    print('任务结束，去重后的数据存入{0}\n'.format(file_save))
    
##网络爬虫模块结束

####################################################################
#主循环

root = Tk()
    
def main():
    root.title('网络爬虫0.6版')
    root.geometry('500x500+200+100')  #窗口大小，位置
    root.maxsize(1000, 1000)          #窗口最大尺寸
    root.minsize(500, 500)


    app = App(master=root)            #初始化窗口
    app.mainloop()                    #进入消息循环


if __name__ == '__main__':
    main()

#End
