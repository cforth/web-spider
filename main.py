#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''主函数'''

from spider.spider import *
from spider.gui import *

root = Tk()
root.title('网络爬虫1.0版')    

#url_head = 'http://book.douban.com/subject/'
#start = 4866901
#end = 4866912    

rules = {   'title':r'<title>(.*)</title>',
            'keywords':r'<meta name="keywords" content="(.*?)">',         #不贪婪匹配
            'intro':r'<div class="intro"><p>(.*?)</p>',                   #不贪婪匹配
            'price':r'定价:</span>(.*?)<br/>'}                            #不贪婪匹配

# rules = {   'stock_id':r'\d+\.S[ZH]',                                        #正则匹配股票代码
            # 'price_inid':r'<span id="ctl04_lbSpj">(\d+\.\d+)</span>',        #正则匹配初始价
            # 'price_target':r'<span id="ctl04_txTgtPrice">(\d+\.\d+)</span>', #正则匹配目标价
            # 'grade':r'<span id="ctl04_bgpj">([\u4e00-\u9fa5]+)</span>',      #正则匹配评级
            # 'trade':r'<span id="ctl04_lbHylbmc">([\u4e00-\u9fa5]+)</span>'}  #正则匹配行业

spider = Spider(rules)
app = App(spider, master=root)               #初始化GUI
app.mainloop()                               #进入消息循环

