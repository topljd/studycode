'''
url:http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
Form Data:里面的数据
i: love
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15905659126969
sign: 523ebfea78343c86224d97f1ed26b13e
ts: 1590565912696
bv: 0ea2f265e69dc7094ed5f0b64ef39e0b
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
这里会发现salt不一样
'''
import requests
import time
import random
import hashlib
import tkinter as tk
import json
#code = input('请输入您想要查询的字符串')

def make_md5(string):
    string = string.encode('utf-8')
    md5 = hashlib.md5(string).hexdigest()#加密规则
    return md5

def translate():
    # 1590568536.0856183
    ts = str(int(time.time() * 1000))
    salt = ts + str(random.randint(0, 9))
    #  sign: n.md5("fanyideskweb" + e + i + )
    sign = make_md5('fanyideskweb' + t1.get(0.0,'end') + salt + "Nw(nmmbP%A-r6U3EUn]Aj")
    bv = make_md5(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")
    data = {
        'i': t1.get(0.0,'end'),
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    headers = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '244',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=388431629@10.169.0.83;JSESSIONID=aaaR4nS2VfKiJg3Qaovjx;OUTFOX_SEARCH_USER_ID_NCOO=1840796087.236859;___rl__test__cookies=1590569427103',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/81.0.4044.138Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    text = requests.post('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule', data=data,
                         headers=headers)
    t1.delete(0.0,'end')
    text = json.loads(text.text)#json将字符串转为字典类型（本身就是字典型的字符串）
    result = text["translateResult"][0][0]["tgt"]
    t1.insert(0.0,result)

#无界面 程序立即结束 其实有界面刷新一下就立马消失
root = tk.Tk()
root.geometry('500x250')#设计宽和高  x这是英文字母x
root.title('翻译小程序')

b1 = tk.Button(root,text='一键翻译',command=translate)
b1.pack()

t1 = tk.Text(root)#将文本主键填到root文本中
t1.pack()
root.mainloop()#无线循环


