from selenium import webdriver
from lxml import etree
from time import sleep
import csv
from helper import Chapter,Lesson
# 加启动配置
option = webdriver.ChromeOptions()
#option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument('-headless')
# 打开chrome浏览器
driver = webdriver.Chrome(options=option)
#url = 'https://study.163.com/course/introduction.htm?courseId=1005084022#/courseDetail?tab=1'
url = 'https://study.163.com/course/introduction.htm?courseId=1005084022#/courseDetail?tab=1'
driver.get(url)
sleep(10)
text = driver.page_source
print(text)
driver.quit()
# with open('text.html','w',encoding='utf-8') as f:
#     f.write(text)
#解析数据
html = etree.HTML(text)
#获取章节
lessons = html.xpath('//div[@class="section"]')#本网页有15个章节
for lesson in lessons:
    ks = lesson.xpath('./span[1]/text()')
    name = lesson.xpath('./span[3]/text()')
    title = ks[0]+' '+name[0]
    print(title)
    with open('title.txt','a',encoding='utf-8') as f:
        f.write(title+'\n')




# TABLEHEAD = ['章节号', '章节名', '课时号', '课时名', '课时长']
# rows = []
# for each in chapters:
#     chapter = Chapter(each)
#     lessons = chapter.get_lessons()
#     for each in lessons:
#         lesson = Lesson(each)
#         chapter_info = chapter.chapter_info
#         lesson_info = lesson.lesson_info
#         values = (*chapter_info, *lesson_info)
#         row = dict(zip(TABLEHEAD, values))
#         rows.append(row)
# # 存储数据
# with open('courseinfo.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.DictWriter(f, TABLEHEAD)
#     writer.writeheader()
#     writer.writerows(rows)