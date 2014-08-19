#coding=utf-8  

import urllib  
import urllib2  

url = 'http://localhost/login.php'  

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 

values = {'user' : 'chaif',  
          'pass' : '888888' }  

headers = { 'User-Agent' : user_agent } 
data = urllib.urlencode(values) #处理数据
req = urllib2.Request(url, data, headers) #发送请求同时传data表单 
response = urllib2.urlopen(req)  #接受反馈的信息
the_page = response.read()  #读取反馈的内容
print the_page  
