#抓取股票关注
#python3.4.1

import urllib.request   #网络模块
import re               #正则表达式模块

def get_stock_info(url):
    response = urllib.request.urlopen(url)  #抓取网页
    text = response.read()
    stock_name = re.findall(r'\d+\.S[ZH]', str(text)) #正则匹配stock name
    price = re.findall(r'\d+\.\d+', str(text)) #正则匹配price
    if len(stock_name) != 0:
        name = stock_name[0]
        sname = '1' + name[0:6] if name[-1] == 'Z' else '0' + name[0:6]
        return '  [\"{0}\", \"\", \"date\", \"{1}\",  \"{2}\",  \"buy\"],\n'.format(sname, price[2], price[3])
    else:
        return ''

def write_stock_file(mystr):
    f = open('f:/temp/workfile.txt', 'w')
    f.write(str(mystr))
    f.close()

#主程序开始
mystr = ''
url_head = 'hhh' #需替换
url_tail = 'ttt' #需替换
start_id = 1     #需替换
end_id = 10      #需替换

#批量访问网页，抓取数据，写入文件。
for i in range(end_id, start_id, -1):
    mystr = mystr + get_stock_info(url_head + str(i) + url_tail)

write_stock_file(mystr)
 
#主程序结束

