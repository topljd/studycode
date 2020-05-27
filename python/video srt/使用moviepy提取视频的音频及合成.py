'''
使用moviepy提取视频的音频及合成
提取 a.mp4 的音频部分。
然后把提取到的音频添加到 b.mp4 里
'''
from moviepy.editor import *


#读取2个视频
videoclip_1 = VideoFileClip('data/a.mp4')
videoclip_2 = VideoFileClip('data/b.mp4')

#提取第一个视频文件的音频部分
audio_1 = videoclip_1.audio
#生成音频文件
audio_1.write_audiofile('data/audio_1.mp3')



#将提取音频和第二个视频文件进行合成
videoclip_3 = videoclip_2.set_audio(audio_1)

#输出心得视频文件
videoclip_3.write_videofile('data/c.mp4')
