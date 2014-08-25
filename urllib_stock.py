#抓取股票关注
#python3.4.1

import urllib.request   #网络模块
import re               #正则表达式模块

def get_stock_info(url):
    """抓取网页，利用正则表达式匹配股票名称stock_name与价格price。
    当stock_name存在时返回匹配后处理的
    """
    response = urllib.request.urlopen(url)  #抓取网页
    text = response.read()
    stock_name = re.findall(r'\d+\.S[ZH]', str(text)) #正则匹配stock name
    price = re.findall(r'\d+\.\d+', str(text)) #正则匹配price
    if len(stock_name) != 0:
        name = stock_name[0]
        sname = '1' + name[0:6] if name[-1] == 'Z' else '0' + name[0:6]
        return '  ["{0}", "", "2014-08-25", "{1}",  "{2}",  "买入"],\n'.format(sname, price[2], price[3])
    else:
        return ''

def write_stock_file(mystr):
    """以写入方式打开文件，写入字符串mystr并自动关闭文件。
    """
    with open('f:/temp/workfile.txt', 'w') as f:
        f.write(str(mystr))


def main():
    """设置网页抓取地址头部、页面ID范围、地址尾部。
    合成需要抓取的网页地址，在ID范围内循环抓取数据存储在mystr中。
    最后写入文件。
    """
    mystr = ''
    url_head = 'hhh' #需替换
    url_tail = 'ttt' #需替换
    start_id = 1     #需替换
    end_id = 10      #需替换

    for i in range(end_id, start_id, -1):
        mystr = mystr + get_stock_info(url_head + str(i) + url_tail)

    write_stock_file(mystr)
 
