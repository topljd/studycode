from urllib import request
resp = request.urlopen('http://www.baidu.com')
#print(resp.read())#获取百度页面的源码
#终端打印出来的字符串是Arscii码
# print(resp.read(10))#b'<!DOCTYPE ' 前十个字符
# print(resp.readline())#b'html><!--STATUS OK-->\n'  获取一行
# print(resp.readlines())#获取多行



'''
urlretrieve 
将网页上的一个文件保存到本地,下载一个网页、图片
'''
from urllib import request
#下载网页 urlretrieve
#request.urlretrieve('http://www.baidu.com',"files/baidu.html")

#下载图片 urlretrieve
#request.urlretrieve('https://static.veer.com/veer/static/resources/keyword/2020-02-19/533ed30de651499da1c463bca44b6d60.jpg',"files/tupian.jpg")

'''
urlencode函数：
对URL中包含了中文或者其他特殊字符，进行编码
'''
from urllib import parse
# params = {'name':'张三','age':18,'greet':'hello world'}
# result = parse.urlencode(params)
# print(result)#name=%E5%BC%A0%E4%B8%89&age=18&greet=hello+world


# url = 'http://www.baidu.com/s?wd=刘德华'
# resp = request.urlopen(url)
# print(resp.read())#现在ascii报错，不能出现中文

# url = 'http://www.baidu.com/s'
# params = {'wd':'刘德华'}
# qs = parse.urlencode(params)
# url = url + '?'+qs
# print(url)
# resp = request.urlopen(url)
# print(resp.read())

'''
parse_qs函数：
经过编码后的URL参数进行解码，示例代码如下：
'''
# from urllib import parse
# params = {'name':'张三','age':'18','greet':'hello world'}
# qs = parse.urlencode(params)
# print(qs)
# result = parse.parse_qs(qs)
# print(result)
# name=%E5%BC%A0%E4%B8%89&age=18&greet=hello+world
# {'name': ['张三'], 'age': ['18'], 'greet': ['hello world']}


'''
urlaprse  与  urlsplit
这两个基本是一模一样的，唯一不一样的是urlparse多了一个params属性
'''
# from urllib import parse
# url = 'http://www.baidu.com/s?wd=python&username=abc#1'
# result = parse.urlparse(url)
# print(result)
#ParseResult(scheme='http', netloc='www.baidu.com', path='/s', params='', query='wd=python&username=abc', fragment='1')
#print('scheme',result.scheme)#scheme http

# result1 = parse.urlsplit(url)
# print(result1)
#SplitResult(scheme='http', netloc='www.baidu.com', path='/s', query='wd=python&username=abc', fragment='1')

