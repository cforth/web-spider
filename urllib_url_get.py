#python3.4.1

import urllib
import urllib.request   #网络模块
import re               #正则表达式模块

#用get方式访问网址
keyword = '福建'

data = {}
data['channelid'] = '200043'
data['templet'] = 'fj_web_2012.jsp'
data['sortfield'] = '-docreltime'
data['searchword'] = keyword
data['classsql'] = ''
data['keyword'] = keyword

url_values = urllib.parse.urlencode(data)
print(url_values)

url = 'http://www.fujian.gov.cn/was5/web/search'
full_url = url + '?' + url_values

html = urllib.request.urlopen(full_url).read()
html.rstrip()

myurl = re.findall(r'[\u4e00-\u9fa5，。；“”’‘：]+', str(html.decode('utf8'))) #匹配中文字符及标点符号

for c in myurl: 
    print(c) #显示匹配的结果，不能完全匹配
