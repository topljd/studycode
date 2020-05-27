'''
使用正则表达式headers转换成python字典格式的工具
'''
import re
headers = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Connection: keep-alive
Content-Length: 244
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: OUTFOX_SEARCH_USER_ID=388431629@10.169.0.83; JSESSIONID=aaaR4nS2VfKiJg3Qaovjx; OUTFOX_SEARCH_USER_ID_NCOO=1840796087.236859; ___rl__test__cookies=1590569427103
Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Referer: http://fanyi.youdao.com/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
X-Requested-With: XMLHttpRequest
"""
header = ''
for i in headers:
    if i == ':':
        i = "':'"
    if i == '\n':
        i = "',\n'"
    header += i
print(header[2:].replace(' ', '')+'\'')
