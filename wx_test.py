# -*- coding: utf-8 -*-
# 网络爬虫0.6版
# Python 2.7
import wx
import urllib2
import urllib
import re

def get_stock_info(url):
    """抓取网页，利用正则表达式匹配股票信息。
    网页请求头部为Chrome信息，网页编码为gb2312。
    若网页中股票代码存在，返回股票信息。
    """
    user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.6 Safari/537.36'
    req = urllib2.Request(url)
    req.add_header('User-Agent', user_agent)

    response = urllib2.urlopen(req)  #抓取网页      
    text = response.read().decode('gb2312')

    stock_id = re.findall(r'\d+\.S[ZH]', text)                                             #正则匹配股票代码
    price_inid = re.findall(r'<span id="ctl04_lbSpj">(\d+\.\d+)</span>', text)             #正则匹配初始价
    price_target = re.findall(r'<span id="ctl04_txTgtPrice">(\d+\.\d+)</span>', text)      #正则匹配目标价
    grade = re.findall(u'<span id="ctl04_bgpj">([\u4e00-\u9fa5]+)</span>', text)           #正则匹配评级
    trade = re.findall(u'<span id="ctl04_lbHylbmc">([\u4e00-\u9fa5]+)</span>', text)       #正则匹配行业
    if len(trade) == 0:
        trade = u'无'
    stock_date = re.findall(r'<span id="ctl04_lblzhxgrq" style="display:inline-block;width:90%;">(\d+\-\d+\-\d+)</span>', text)   #正则匹配日期
    
    if len(stock_id) != 0:
        name = stock_id[0]
        
        if name[-1] == 'Z':
            sname = '1' + name[0:6]
        else:
            sname = '0' + name[0:6]
        return '%s, %s, %s, %s, %s, %s \n' % (sname, trade[0], stock_date[0], price_inid[0], price_target[0], grade[0])
    else:
        return ''


def spider_go(url_head, start, end):
    start = int(start)
    end = int(end)

    mystr = ''
    task_id = 1
    task_all = end - start + 1
    
    for i in range(end, start - 1, -1):
        mystr = mystr + get_stock_info(url_head + str(i))
        task_id = task_id + 1
        
    return mystr
    

def spider(event):
        url = urlname.GetValue()
        start_id = startid.GetValue()
        end_id = endid.GetValue()
        mystr = spider_go(url, start_id, end_id)
        contents.SetValue(mystr)


app = wx.App()
win = wx.Frame(None, title=u"十八哥的网络爬虫", size=(500, 500))
bkg = wx.Panel(win)


loadButton = wx.Button(bkg, label=u'抓取')
loadButton.Bind(wx.EVT_BUTTON, spider)

urlname = wx.TextCtrl(bkg, size=(50,21))
startid = wx.TextCtrl(bkg, size=(50,21))
endid = wx.TextCtrl(bkg, size=(50,21))
contents = wx.TextCtrl(bkg, pos=(5, 35), style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(urlname, proportion=1, flag=wx.EXPAND)
hbox.Add(startid, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(endid, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)


vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1,
         flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()
