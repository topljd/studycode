import re

#输入字符串
str = '''
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html; charset=utf-8
Date: Wed, 03 Jun 2020 14:35:04 GMT
'''
pattern = re.compile('(.*?): (.*?)\n')
result = pattern.findall(str)
for data in result:
    print('\''+data[0]+'\': '+'\''+data[1]+'\',')