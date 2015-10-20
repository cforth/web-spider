#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''主函数'''

from spider.spider import *
from spider.gui import *

root = Tk()
root.title('网络爬虫1.0版')    

#下面是一个示例,设置窗口程序中的四个参数，分别为网址前端，网址后端的起始号码到终止号码，以及数据保存的名称。
#url_head = 'http://book.douban.com/subject/'
#start = '4866901'
#end = '4866912'
#file_name = 'finds'   

#rules是一个字典，内部为正则表达式匹配规则，默认为不贪婪匹配。
rules = {   'title':r'<title>(.*)</title>',                               #匹配豆瓣图书的名称
            'keywords':r'<meta name="keywords" content="(.*?)">',         #匹配图书的关键词
            'intro':r'<div class="intro"><p>(.*?)</p>',                   #匹配图书的简介
            'price':r'定价:</span>(.*?)<br/>'}                            #匹配图书的定价

#以下rules是我个人用于股票关注数据抓取的规则。
# rules = {   'stock_id':r'\d+\.S[ZH]',                                        #匹配股票代码
            # 'price_inid':r'<span id="ctl04_lbSpj">(\d+\.\d+)</span>',        #匹配初始价
            # 'price_target':r'<span id="ctl04_txTgtPrice">(\d+\.\d+)</span>', #匹配目标价
            # 'grade':r'<span id="ctl04_bgpj">([\u4e00-\u9fa5]+)</span>',      #匹配评级
            # 'trade':r'<span id="ctl04_lbHylbmc">([\u4e00-\u9fa5]+)</span>'}  #匹配行业

spider = Spider(rules)                       #初始化爬虫模块
app = App(spider, master=root)               #初始化GUI模块
app.mainloop()                               #进入GUI模块消息循环

