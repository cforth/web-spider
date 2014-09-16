# -*- coding: utf-8 -*-
# 网络爬虫
# 通用网络爬虫实现
# 根据提供的匹配规则和网址来匹配一切网页内容
# Python 2.7

import urllib2
import urllib
import chardet    #检测网页编码
import re
import codecs
from time import time

def write_file(mystr, file_name):
    """以写入方式打开文件，默认文件字符编码为utf-8，写入字符串mystr并自动关闭文件。
    """
    with codecs.open(file_name, 'a', 'utf-8') as f:
        f.write(mystr)


def get_url_info(url):
    """抓取网页内容
    网页请求头部为Chrome信息，被抓取网页的编码为gb2312。
    返回包含网页内容的字符串。
    """
    user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.6 Safari/537.36'
    req = urllib2.Request(url)
    req.add_header('User-Agent', user_agent)

    data = urllib2.urlopen(req).read()            #抓取网页
    html_code = chardet.detect(data)              #通过chardet模块检测编码
    return data.decode(html_code['encoding'])     


def match_text(text, rules):
    """根据正则表达式匹配目标文本
    text为被分析的文本字符串。
    text去除每行行首与行尾空白字符、空行
    rules为一个字典，键为匹配目标名称，值为匹配规则（正则表达式字符串）。
    函数返回一个字典，键为匹配目标名称，值为符合匹配规则的字符串列表。
    """
    text = re.sub('\s*\n\s*','', text)            #去除每行行首与行尾空白字符、空行
    
    find_dict = {}
    
    for key in rules :
        s = re.findall(rules[key], text)
        find_dict[key] = s

    return find_dict   


class Spider():
    """网页爬虫类
    从标准输入获取网址url_head、起始页序号start、终止页序号end
    self.finds为存储抓取结果的字典，self.finds_str为抓取结果转为字符串
    """
    def __init__(self, rules, url_head, start, end):
        self.rules = rules
        self.url_head = url_head
        self.start = start
        self.end = end    
        self.finds = {}
        self.finds_str = ''

    def catch(self):
        """根据匹配规则批量抓取一些网页
        顺序为页码从大到小，函数返回一个包含所有匹配目标信息的字典。
        """
        for i in range(self.start, self.end + 1, 1):
            text = get_url_info(self.url_head + str(i))
            find_dict = match_text(text, self.rules)
            self.finds[str(i)] = find_dict

    def format_finds(self):
        """格式化输出抓取结果
        将字典根据key进行排序后转为字符串
        """
        finds_list = sorted(self.finds.items(), key=lambda d:d[0])
        for lst in finds_list :
            self.finds_str += '%s :\n' % lst[0]
            for key, value in lst[1].items() :
                self.finds_str += '  %s :\n' % key
                for v in value:
                    self.finds_str += '    %s\n' % v
            self.finds_str += '\n\n'

    def save_finds(self, file_name):
        """将抓取结果字符串写入文件
        """
        write_file(self.finds_str, file_name)




def main():
    t = time()         #记录程序运行开始时间
    
##    stock_rules = {'stock_id':'\d+\.S[ZH]',                                         #正则匹配股票代码
##             'price_inid':'<span id="ctl04_lbSpj">(\d+\.\d+)</span>',               #正则匹配初始价
##             'price_target':'<span id="ctl04_txTgtPrice">(\d+\.\d+)</span>',        #正则匹配目标价
##             'grade':u'<span id="ctl04_bgpj">([\u4e00-\u9fa5]+)</span>',            #正则匹配评级
##             'trade':u'<span id="ctl04_lbHylbmc">([\u4e00-\u9fa5]+)</span>',        #正则匹配行业
##             'stock_date':'<span id="ctl04_lblzhxgrq" style="display:inline-block;width:90%;">(\d+\-\d+\-\d+)</span>'}  #正则匹配日期
##    url_head = str(raw_input(u'请输入网址前部：\n'))
##    start = int(raw_input(u'请输入页面开始ID：\n'))
##    end = int(raw_input(u'请输入页面结束ID：\n'))
    

    book_rules = {'title':u'<title>(.*)</title>',
                  'keywords':u'<meta name="keywords" content="(.*?)">', #不贪婪匹配
                  'intro':u'<div class="intro"><p>(.*?)</p>'}           #不贪婪匹配
    url_head = 'http://book.douban.com/subject/'
    start = 4866934
    end = 4866943
    
    my_spider = Spider(book_rules, url_head, start, end)
    my_spider.catch()
    my_spider.format_finds()
    my_spider.save_finds('f:/111.txt')

    print "total run time:"
    print time() - t   #记录程序运行总时间

if __name__ == '__main__' :
    main()
    
# end
