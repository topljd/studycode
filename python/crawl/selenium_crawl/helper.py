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