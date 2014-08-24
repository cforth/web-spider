#抓取网页，转换编码为utf-8
#python3.4.1

import urllib.request   #网络模块
import re               #正则表达式模块

html = urllib.request.urlopen("http://www.cfishacker.com/blog").read()
myurl = re.findall(r'href="[\w\/\.-]+">[\u4e00-\u9fa5《》、\s\w\\.-]+', str(html.decode('utf8')))  #匹配所有网址和网址标题（包含中文）

for c in myurl:
    result = c[6:].replace('">',' ')  
    print('网址：{0}'.format(result)) #显示匹配的结果，不能完全匹配
