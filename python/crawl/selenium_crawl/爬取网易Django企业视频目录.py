from selenium import webdriver
from lxml import etree
from time import sleep
import csv
class Chapter:
    def __init__(self, chapter):
        self.chapter = chapter
        self._chapter_info = None

    def parse_all(self):
        # 章节号
        chapter_num = self.chapter.xpath(
            './/span[contains(@class, "chaptertitle")]/text()')[0]
        # 去掉章节号最后的冒号
        chapter_num = chapter_num[:-1]
        # 章节名
        chapter_name = self.chapter.xpath(
            './/span[contains(@class, "chaptername")]/text()')[0]
        return chapter_num, chapter_name

    @property
    def chapter_info(self):
        self._chapter_info = self.parse_all()
        return self._chapter_info

    def get_lessons(self):
        return self.chapter.xpath(
            './/div[@data-lesson]')


class Lesson:
    def __init__(self, lesson):
        self.lesson = lesson
        self._lesson_info = None

    @property
    def lesson_info(self):
        # 课时号
        lesson_num = self.lesson.xpath(
            './/span[contains(@class, "ks")]/text()')[0]
        # 课时名
        lesson_name = self.lesson.xpath(
            './/span[@title]/@title')[0]
        # 课时长
        lesson_len = self.lesson.xpath(
            './/span[contains(@class, "kstime")]/text()')[0]
        self._lesson_info = lesson_num, lesson_name, lesson_len
        return self._lesson_info
# 加启动配置
option = webdriver.ChromeOptions()
#option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument('-headless')
# 打开chrome浏览器
driver = webdriver.Chrome(options=option)
url = 'https://study.163.com/course/introduction.htm?courseId=1005084022#/courseDetail?tab=1'
driver.get(url)
text = driver.page_source
print(text)
driver.quit()
# with open('text.txt','w',encoding='utf-8') as f:
#     f.write(text)
#解析数据
html = etree.HTML(text)
#获取章节
chapters = html.xpath('//div[@class="chapter"]')
TABLEHEAD = ['章节号', '章节名', '课时号', '课时名', '课时长']
rows = []
for each in chapters:
    chapter = Chapter(each)
    lessons = chapter.get_lessons()
    for each in lessons:
        lesson = Lesson(each)
        chapter_info = chapter.chapter_info
        lesson_info = lesson.lesson_info
        values = (*chapter_info, *lesson_info)
        row = dict(zip(TABLEHEAD, values))
        rows.append(row)
# 存储数据
with open('courseinfo.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, TABLEHEAD)
    writer.writeheader()
    writer.writerows(rows)