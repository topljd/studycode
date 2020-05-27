#安装 moviepy 模块 pip install moviepy


'''
1、从视频中提取音频
安装 pip install moviepy
'''
audio_file = work_path+'\\out.wav'
video = VideoFileClip(video_file)
video.audio.write_audiofile(audio_file,ffmpeg_params=['-ar','16000','-ac','1'])


'''
2、根据静音对音频分段
pip install pydub
#第一种方法
# 这里silence_thresh是认定小于-70dBFS以下的为silence，发现小于 sound.dBFS * 1.3 部分超过 700毫秒，就进行拆分。这样子分割成一段一段的。
sounds = split_on_silence(sound, min_silence_len = 500, silence_thresh= sound.dBFS * 1.3)
sec = 0
for i in range(len(sounds)):
    s = len(sounds[i])
    sec += s
print('split duration is ', sec)
print('dBFS: {0}, max_dBFS: {1}, duration: {2}, split: {3}'.format(round(sound.dBFS,2),round(sound.max_dBFS,2),sound.duration_seconds,len(sounds)))
'''
#第二种方法
# 通过搜索静音的方法将音频分段
# 参考：https://wqian.net/blog/2018/1128-python-pydub-split-mp3-index.html
timestamp_list = detect_nonsilent(sound, 500, sound.dBFS * 1.3, 1)

for i in range(len(timestamp_list)):
    d = timestamp_list[i][1] - timestamp_list[i][0]
    print("Section is :", timestamp_list[i], "duration is:", d)
print('dBFS: {0}, max_dBFS: {1}, duration: {2}, split: {3}'.format(round(sound.dBFS, 2), round(sound.max_dBFS, 2),sound.duration_seconds,len(timestamp_list)))


'''
#获取Access Token
使用百度Ai产品需要授权，一定量是免费的，生成字幕够用了
'''
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode( 'utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.errno))
        result_str = err.reason
    if (IS_PY3):
        result_str =  result_str.decode()


    print(result_str)
    result = json.loads(result_str)
    print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        print(SCOPE)
        if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
            raise DemoError('scope is not correct')
        print('SUCCESS WITH TOKEN: %s  EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')

'''
4、使用Raw数据进行合成
这里使用百度语音极速版来合成文字，因为官方介绍专有GPU服务集群，识别响应速度较标准版API提升2倍及识别准确率提升15%。适用于近场短语音交互，如手机语音搜索、聊天输入等场景。 支持上传完整的录音文件，录音文件时长不超过60秒。实时返回识别结果

'''
def asr_raw(speech_data, token):
    length = len(speech_data)
    if length == 0:
        # raise DemoError('file %s length read 0 bytes' % AUDIO_FILE)
        raise DemoError('file length read 0 bytes')


    params = {'cuid': CUID, 'token': token, 'dev_pid': DEV_PID}
    #测试自训练平台需要打开以下信息
    #params = {'cuid': CUID, 'token': token, 'dev_pid': DEV_PID, 'lm_id' : LM_ID}
    params_query = urlencode(params)


    headers = {
        'Content-Type': 'audio/' + FORMAT + '; rate=' + str(RATE),
        'Content-Length': length
    }


    url = ASR_URL + "?" + params_query
    # print post_data
    req = Request(ASR_URL + "?" + params_query, speech_data, headers)
    try:
        begin = timer()
        f = urlopen(req)
        result_str = f.read()
        # print("Request time cost %f" % (timer() - begin))
    except  URLError as err:
        # print('asr http response http code : ' + str(err.errno))
        result_str = err.reason


    if (IS_PY3):
        result_str = str(result_str, 'utf-8')
    return result_str

'''
5、生成字幕
字幕格式： https://www.cnblogs.com/tocy/p/subtitle-format-srt.html

生成字幕其实就是语音识别的应用，将识别后的内容按照 srt 字幕格式组装起来就 OK 了。具体字幕格式的内容可以参考上面的文章，代码如下：
'''
idx = 0
for i in range(len(timestamp_list)):
    d = timestamp_list[i][1] - timestamp_list[i][0]
    data = sound[timestamp_list[i][0]:timestamp_list[i][1]].raw_data
    str_rst = asr_raw(data, token)
    result = json.loads(str_rst)
    # print("rst is ", result)
    # print("rst is ", rst['err_no'][0])


    if result['err_no'] == 0:
        text.append('{0}\n{1} --> {2}\n'.format(idx, format_time(timestamp_list[i][0]/ 1000), format_time(timestamp_list[i][1]/ 1000)))
        text.append( result['result'][0])
        text.append('\n')
        idx = idx + 1
        print(format_time(timestamp_list[i][0]/ 1000), "txt is ", result['result'][0])
with open(srt_file,"r+") as f:
    f.writelines(text)

