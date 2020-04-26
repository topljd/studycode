### vip视频免费看
`因为刚开始，需要安装requests库 pip install requests`
找到vip的视频地址url
找到jx.618g.com/?url=加入网址
进行解析，F12看里面的源码
发现后面的视频地址规律
https://baidu.com-l-baidu.com/20190121/10955_dd78dee4/1000k/hls/45e86ff0d43000005.ts

下载好了需要拼接
进入cmd进入文件的目录
copy /b *.ts 111.mp4

http://jx.618g.com/?url=https://v.qq.com/x/cover/79npj83isb0ylvq/t0029x7d5pl.html
网页中含有/m3u8-dp.php?url=https://baidu.com-l-baidu.com/20190121/10955_dd78dee4/index.m3u8
解析的网址 https://baidu.com-l-baidu.com/20190121/10955_dd78dee4/1000k/hls/index.m3u8
---
http://jx.618g.com/?url=https://www.iqiyi.com/v_19rygmp54o.html
/m3u8-dp.php?url=https://youku.cdn10-okzy.com/20200421/14278_62c417e9/index.m3u8
https://youku.cdn10-okzy.com/20200421/14278_62c417e9/1000k/hls/index.m3u8

    