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

'''
request.Request类：
如果想要在请求的时候有请求头，必须使用上面类来实现.比如User-agent
'''
# from urllib import  request
# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# resp = request.urlopen(url)
# print(resp.read())
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
# }
# req = request.Request(url,headers=headers)
# resp = request.urlopen(req)
# print(resp.read())#此时返回的是全部的网页内容

'''

'''
from urllib import  request
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8D%97%E4%BA%AC&needAddtionalResult=false'
headers = {
    'cookie': 'JSESSIONID=ABAAABAABEIABCI49A59631DE939FF2FB32C9BBC26AC1CA; WEBTJ-ID=20200602125437-1727361a1c62d5-05725b5d450a36-f7d1d38-1049088-1727361a1c7580; RECOMMEND_TIP=true; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; user_trace_token=20200602125435-dd5c8aff-be8f-4dc6-adf4-520c3432e119; LGSID=20200602125435-34eecd63-5609-44c0-93d4-5a5bbb5368f3; PRE_SITE=https%3A%2F%2Fwww.lagou.com; LGUID=20200602125435-e72a5007-38f3-4a45-955c-54ca15e51890; _ga=GA1.2.1011798515.1591073679; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591073679; _gid=GA1.2.1738248546.1591073679; index_location_city=%E6%B1%9F%E8%8B%8F; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221727361f4f13f8-028a7ebc86c8c4-f7d1d38-1049088-1727361f4f24ca%22%2C%22%24device_id%22%3A%221727361f4f13f8-028a7ebc86c8c4-f7d1d38-1049088-1727361f4f24ca%22%7D; sajssdk_2015_cross_new_user=1; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=c6573ee4cb77628f2574701951b0e699a80155a7ac; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591074755; LGRID=20200602131304-6b549400-f02c-4d1e-b605-7403dae21409; SEARCH_ID=9fd23d5d0dc34dd8b1c7b9572fad95c6',
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python/p-city_79?px=default',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}
data = {
    'first':'true',
    'pn':1,
    'kd':'python'
}
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))