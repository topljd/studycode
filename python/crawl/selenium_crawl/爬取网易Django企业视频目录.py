from selenium import webdriver
from time import sleep

# 加启动配置
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])

# 打开chrome浏览器
driver = webdriver.Chrome(options=option)
driver.get("https://www.baidu.com")
sleep(10)
driver.quit()