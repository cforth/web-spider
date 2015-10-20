#网络爬虫1.0版

![web-spider](http://img3.douban.com/view/photo/photo/public/p2276327233.jpg)

使用Python3实现的网络爬虫，模块化设计后的1.0版本。

##使用举例

1. 设置网页抓取的正则匹配规则，修改main.py中的rules变量：
  ```
  rules = {   'title':r'<title>(.*)</title>',                     #匹配豆瓣图书的名称
            'keywords':r'<meta name="keywords" content="(.*?)">', #匹配图书的关键词
            'intro':r'<div class="intro"><p>(.*?)</p>',           #匹配图书的简介
            'price':r'定价:</span>(.*?)<br/>'}                    #匹配图书的定价
  ```

2. 运行main.py
  ```
  python3 main.py
  ```

3. 在窗口程序中设置四个参数，点击“点击抓取”按钮。抓取结果保存在磁盘文件中。参考设置如下：
  ```
  #url_head = 'http://book.douban.com/subject/'
  #start = '4866901'
  #end = '4866912'
  #file_name = 'finds' 
  ```

##不再维护的版本：

###[**窗口程序tk版**](https://github.com/cforth/web-spider/blob/master/old/tkinter_spider.py)
Python 3 GUI库tkinter实现。

###[**通用版**](https://github.com/cforth/web-spider/blob/master/old/spider.py)
根据提供的正则表达式匹配规则，网页地址，页码范围，获取所有匹配的内容，以字典形式返回。

###[**命令行版**](https://github.com/cforth/web-spider/blob/master/old/text_spider.py)
命令行实现，抓取特定股票行情网页的股票数据。

###[**窗口程序wx版**](https://github.com/cforth/web-spider/blob/master/old/wx_spider.py)
Python 2.7.6 GUI库wx实现。
