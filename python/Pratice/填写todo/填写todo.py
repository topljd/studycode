import pyautogui
import time
import pyperclip
#copy('str1')                   复制内容str1，内容可设置为中文等
#paste()　　　　　　　将复制的内容粘贴到输入处，粘贴时也可使用pyautogui的hotkey实现
file = open(r'G:\python\crawl\selenium_crawl\title.txt',encoding='utf-8')
for line in file:
    print(line[:-1])
    # 左击一次
    pyautogui.click(x=218, y=639, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
    # 输入文字
    #pyautogui.typewrite(message=line[:-2], interval=0.001)  只能输入英文

    #输入中文
    pyperclip.copy(line[:-1])
    pyautogui.hotkey('ctrl', 'v')
    # 键盘点击
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
file.close()
#打印鼠标的位置
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX,currentMouseY)



#移动鼠标
#pyautogui.moveTo(x=218, y=639,duration=0.5, tween=pyautogui.linear)

