#coding=utf-8  

import urllib2  

url = 'http://cfishacker.com/stock/'  
response = urllib2.urlopen(url)  #抓取网页内容
the_page = response.read()  
print the_page  
