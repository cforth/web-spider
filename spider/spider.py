#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''网络爬虫主体'''

import urllib.request   #网络模块
import re               #正则表达式模块
import codecs           #文件编码转换
import chardet          #检测网页编码模块
import sys, time, json


def print_list(the_list):
    """格式化输出列表（非嵌套）
    """
    if len(the_list) == 0:
        print('')
    else:
        for each_item in the_list:
            print(each_item)


def print_dict(the_dict, indent=False, level=0):
    """格式化打印出嵌套的字典对象,如果最终值为列表时，使用print_list打印列表
    indent默认为False，不打开缩进特性
    缩进级别level默认为0
    """
    for key, value in list(the_dict.items()) :
        if isinstance(value, dict):
            print('%s:' % key)
            print_dict(value, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='')             
            print('%s:' % key, end='')
            if isinstance(value, list):
                print_list(value)
            else:
                print(value)
    print('\n')


def get_url_info(url):
    """抓取网页内容
    网页请求头部为Chrome信息，被抓取网页的编码通过chardet模块检测。
    返回包含网页内容的字符串。
    """
    user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.6 Safari/537.36'
    req = urllib.request.Request(url)
    req.add_header('User-Agent', user_agent)

    data = urllib.request.urlopen(req).read()     #抓取网页
    html_code = chardet.detect(data)              #通过chardet模块检测编码
    return data.decode(html_code['encoding'])     


class Spider(object):
    """网页爬虫类
    类实例化时，接受rules参数为正则比配规则的字典
    finds为已经抓取到的数据（默认为空字典），delaySecs为每次抓取的延时时间（默认为1秒）
    """
    def __init__(self, rules, finds={}, delaySecs=1):
        self.rules = self.compile_rules(rules)
        self.delaySecs = delaySecs
        self.finds = finds

    def compile_rules(self, rules):
        """预编译正则表达式对象
        """
        reRules = {}
        for key in rules :
            reRules[key] = re.compile(rules[key])
        return reRules

    def match_text(self, text, rules):
        """根据正则表达式匹配目标文本
        text为被分析的文本字符串。
        text去除每行行首与行尾空白字符、空行
        rules为一个字典，键为匹配目标名称，值为经过编译的正则表达式对象。
        函数返回一个字典，键为匹配目标名称，值为符合匹配规则的字符串列表。
        """
        text = re.sub('\s*\n\s*','', text)        #去除每行行首与行尾空白字符、空行
        
        find_dict = {}
        
        for key in rules :
            find_dict[key] = rules[key].findall(text)

        return find_dict   
        
    def queue_init(self, url_head, start, end):
        """生成抓取网页的网址队列
        目前暂时为顺序生成
        """
        return [(url_head + str(i)).replace(' ', '') for i in range(start, end + 1, 1)]

    def catch(self, url_head, start, end, file_name):
        """根据匹配规则批量抓取一些网页
        从标准输入获取网址url_head、起始页序号start、终止页序号end、数据保存文件名file_name
        顺序为页码从小到大，函数返回一个包含所有匹配目标信息的字典。
        """
        print(file_name)
        self.load_finds(file_name)                #从磁盘恢复抓取结果对象

        queue = self.queue_init(url_head, start, end)  #待抓取的网页队列
        the_page = 1
        pages = end - start + 1
        for url in queue:
            try:
                if url not in self.finds:      #判断需抓取的页面是否已经抓取过，抓取过不重复抓取
                    find_dict = self.match_text(get_url_info(url), self.rules)
                    self.finds[url] = find_dict
                    print('页面抓取成功！页面：{0}'.format(url))
                    time.sleep(self.delaySecs)    #设置每次抓取的延时
                else:
                    print('页面抓取结果已存在！不重复抓取！页面：{0}'.format(url))
            except:
                print('网页获取失败！错误信息：{0}'.format(sys.exc_info()[0]))
            print('任务进度({0}/{1})'.format(str(the_page), str(pages)))
            the_page += 1
        
        self.save_finds(file_name)                #将抓取结果对象保存至磁盘
        print_dict(self.finds, indent=True)       #格式化输出抓取结果对象
    
    def save_finds(self, file_name):
        """将抓取结果字典finds写入磁盘文件,格式为JSON
        """
        try:
            with codecs.open(file_name, 'w', 'utf-8') as f:
                f.write(json.dumps(self.finds))
            print('对象保存成功！文件路径:{0}'.format(file_name))
        except:
            print('对象保存失败！错误信息：{0}'.format(sys.exc_info()[0]))

    def load_finds(self, file_name):
        """将finds对象从磁盘读取并恢复
        """
        try:
            with codecs.open(file_name, 'r', 'utf-8') as f:
                self.finds = json.loads(f.read())
            print('对象读取成功！文件路径:{0}'.format(file_name))
        except:
            print('对象读取失败！finds对象不变！错误信息：{0}'.format(sys.exc_info()[0]))

