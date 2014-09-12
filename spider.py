# -*- coding: utf-8 -*-
# 网络爬虫
# 通用网络爬虫实现
# 根据提供的匹配规则和网址来匹配一切网页内容
# Python 2.7

import urllib2
import urllib
import re

def get_url_info(url):
    """抓取网页内容
    网页请求头部为Chrome信息，被抓取网页的编码为gb2312。
    返回包含网页内容的字符串。
    """
    user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.6 Safari/537.36'
    req = urllib2.Request(url)
    req.add_header('User-Agent', user_agent)

    response = urllib2.urlopen(req)          #抓取网页      
    return response.read().decode('gb2312')  #根据网页编码修改


def match_text(text, rules):
    """根据正则表达式匹配目标文本
    text为被分析的文本字符串。
    rules为一个字典，键为匹配目标名称，值为匹配规则（正则表达式字符串）。
    函数返回一个字典，键为匹配目标名称，值为符合匹配规则的字符串列表。
    """
    find_dict = {}
    
    for key in rules :
        s = re.findall(rules[key], text)
        find_dict[key] = s

    return find_dict   


class Spider():
    """网页爬虫类
    从标准输入获取网址url_head、起始页序号start、终止页序号end
    """
    def __init__(self, rules):
        self.rules = rules
        self.url_head = str(raw_input(u'请输入网址前部：\n'))
        self.start = int(raw_input(u'请输入页面开始ID：\n'))
        self.end = int(raw_input(u'请输入页面结束ID：\n'))
    

        self.finds = {}

    def catch(self):
        """根据匹配规则批量抓取一些网页
        顺序为页码从大到小，函数返回一个包含所有匹配目标信息的字典。
        """
        page = self.end
        for i in range(self.end, self.start - 1, -1):
            text = get_url_info(self.url_head + str(i))
            find_dict = match_text(text, self.rules)
            self.finds[str(page)] = find_dict
            page = page - 1


def main():
    stock_rules = {'stock_id':'\d+\.S[ZH]',                                         #正则匹配股票代码
             'price_inid':'<span id="ctl04_lbSpj">(\d+\.\d+)</span>',               #正则匹配初始价
             'price_target':'<span id="ctl04_txTgtPrice">(\d+\.\d+)</span>',        #正则匹配目标价
             'grade':u'<span id="ctl04_bgpj">([\u4e00-\u9fa5]+)</span>',            #正则匹配评级
             'trade':u'<span id="ctl04_lbHylbmc">([\u4e00-\u9fa5]+)</span>',        #正则匹配行业
             'stock_date':'<span id="ctl04_lblzhxgrq" style="display:inline-block;width:90%;">(\d+\-\d+\-\d+)</span>'}  #正则匹配日期    
    stock_spider = Spider(stock_rules)
    stock_spider.catch()
    print stock_spider.finds

if __name__ == '__main__' :
    main()
    
# end
