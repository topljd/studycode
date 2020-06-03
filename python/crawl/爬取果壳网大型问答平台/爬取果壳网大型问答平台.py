#课题： 爬取果壳问答
#requests
#re
#json


import requests
import re
import json
data_list = []
for page in range(1,101):
    print('++++++++++++++++++++正在爬取第{}页得数据'.format(page))
    #爬虫的一般思路
    #1、分析目标网页，确定爬取的URL路径，headers参数
    base_url = 'https://www.guokr.com/ask/highlight/?page={}'.format(str(page))
    headers = {
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    #2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
    response = requests.get(url=base_url,headers=headers)
    #print(response)#<Response [200]>  表示请求成功

    #提取文本数据用text
    html_data = response.text
    #print(html_data)
    #3、解析数据 -- re模块：提供全部的正则表达式功能
    #<h2><a target="_blank" href="http://www.guokr.com/question/667536/">为什么猪牛羊肉的瘦肉是红色的，鸡肉是粉色的，而鱼肉是白色的？鱼的肌肉里面不充血吗？为什么呢？</a></h2>
    pattern = re.compile('<h2><a target="_blank" href="(.*?)">(.*?)</a></h2>',re.S)#匹配到换行符
    #这里可以推荐css选择器，或者xpath
    pattern_list = pattern.findall(html_data)#返回列表
    #print(pattern_list)#列表里的元组

    #json格式 {result:00,age:{result:00}}[]

    for data in pattern_list:
        data_dict = {}
        data_dict['title'] = data[1]
        data_dict['url']  = data[0]
        data_list.append(data_dict)

    #转换成json
    json_data = json.dumps(data_list,ensure_ascii=False)
    #4、保存数据 -- 保存Json格式的数据
    with open('guoke02.json','w',encoding='utf-8') as f:
        f.write(json_data)


