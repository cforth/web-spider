#抓取股票关注 0.4版
#python3.4.1

import urllib.request   #网络模块
import re               #正则表达式模块
import codecs           #文件编码转换
import sys

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


def spider_go():
    """设置网页抓取地址头部、页面ID范围。
    合成需要抓取的网页地址，在ID范围内循环抓取数据存储在mystr中。
    最后写入文件。
    工作目录为'F:/temp/'。
    """   
    url_head = str(input(u'请输入网址前部：\n'))
    start_id = int(input(u'请输入页面开始ID：\n'))
    end_id = int(input(u'请输入页面结束ID：\n'))
    file_name = 'f:/temp/' + str(input(u'请输入存入的文件名称:\n'))
    mystr = ''
    task_id = 1
    task_all = end_id - start_id + 1

    for i in range(end_id, start_id - 1, -1):
        print('任务进度 ({0}/{1})'.format(task_id, task_all))
        mystr = get_stock_info(url_head + str(i))
        write_stock_file(mystr, file_name)
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
    


