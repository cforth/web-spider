#Catch The Url Error
#python3.4.1

import urllib.request  

url1 = 'http://www.baibai.com/'         # Addrinfo Error
url2 = 'http://bbs.csdn.net/callmewhy'  # 404 Error
url3 = 'http://cfishacker.com/'         # Everything is fine

def url_check(url):
    try:
        urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            return 'The server could\'t fulfill the request. Error code: {0}'.format((e.code))
        elif hasattr(e, 'reason'):
            return 'We failed to reach a server. Reason: {0}'.format(str(e.reason))
    else:
        return 'No exception was raised.'


print('http://www.baibai.com/  -->  %s' % url_check(url1))
print('http://bbs.csdn.net/callmewhy  -->  %s' % url_check(url2))
print('http://cfishacker.com/  -->  %s' % url_check(url3))
