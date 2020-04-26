'''
requests库
pool多线程
'''
import requests
from multiprocessing import Pool
import os

def download(i):
    '''
    下载视频，二进制的  %04d.ts %i
    '''
    url = 'https://baidu.com-l-baidu.com/20190121/10955_dd78dee4/1000k/hls/45e86ff0d4300%04d.ts'% i
    print(url)
    res = requests.get(url)
    ret = res.content
    with open('./vipvideo/{}'.format(url[-10:]),'wb') as f:
        f.write(ret)

if __name__ =='__main__':
    po =Pool(4)
    for i in range(563):
        po.apply_async(download,args=(i,))
    po.close()
    po.join()
