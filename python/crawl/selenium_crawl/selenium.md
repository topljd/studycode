#### 一、selenium简介
selenium最初是一个自动化测试工具,而爬虫中使用它主要是为了解决requests无法直接执行JavaScript代码的问题 selenium本质是通过驱动浏览器，完全模拟浏览器的操作，比如跳转、输入、点击、下拉等，来拿到网页渲染之后的结果，可支持多种浏览器！  
#### 二、环境安装
-  下载安装selennium：pip install selenium
-  下载浏览器驱动程序：
   - http://chromedriver.storage.googleapis.com/index.html
   - http://npm.taobao.org/mirrors/chromedriver
   - 下载后，将chromedriver.exe文件放入chrome的根目录
   - 给谷歌浏览器配置环境变量paht   C:\Program Files (x86)\Google\Chrome\Application
-  查看驱动和浏览器版本的映射关系：
   - http://blog.csdn.net/huilan_same/article/details/51896672

```python
#打开浏览器的代码
from selenium import webdriver
from time import sleep

#后面是你浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')#声明浏览器
#用get打开百度页面
driver.get('http://www.baidu.com')
print(driver.page_source)
driver.close()#关闭浏览器
```

#### 三、简单实用selenium

> 遇到的问题
>
> **1、解决 FileNotFoundError: [WinError 2] 系统找不到指定的文件**
>
> 根据提示找到lib中的subprocess.py文件，CTRL+f查找class Popen模块，再将这个模块中的
> __init__函数中的shell = False 改成shell = True
>
> **2、webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')**驱动的路径

```python
#里面已经有代码失效了，但是原理的话还是可以用的
from selenium import webdriver
from time import sleep

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(r'驱动程序路径')
# 用get打开百度页面
driver.get("http://www.baidu.com")
# 查找页面的“设置”选项，并进行点击
driver.find_elements_by_link_text('设置')[0].click()
sleep(2)
# # 打开设置后找到“搜索设置”选项，设置为每页显示50条
driver.find_elements_by_link_text('搜索设置')[0].click()
sleep(2)

# 选中每页显示50条
m = driver.find_element_by_id('nr')
sleep(2)
m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
m.find_element_by_xpath('.//option[3]').click()
sleep(2)

# 点击保存设置
driver.find_elements_by_class_name("prefpanelgo")[0].click()
sleep(2)

# 处理弹出的警告页面   确定accept() 和 取消dismiss()
driver.switch_to_alert().accept()
sleep(2)
# 找到百度的输入框，并输入 美女
driver.find_element_by_id('kw').send_keys('美女')
sleep(2)
# 点击搜索按钮
driver.find_element_by_id('su').click()
sleep(2)
# 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
driver.find_elements_by_link_text('美女_百度图片')[0].click()
sleep(3)

# 关闭浏览器
driver.quit()
```

#### 四、创建浏览器对象(句柄)

Selenium支持非常多的浏览器，如Chrome、Firefox、Edge等，还有Android、BlackBerry等手机端的浏览器。另外，也支持无界面浏览器PhantomJS。

```python
from selenium import webdriver
browser = webdriver.Chrome()  # 谷歌浏览器
browser = webdriver.Firefox()  # 火狐浏览器
browser = webdriver.Edge()  #IE 浏览器
browser = webdriver.PhantomJS()  # 无可视化界面的浏览器(无头浏览器)
browser = webdriver.Safari()  # 苹果macOS中浏览器
```

#### 五、元素定位

webdriver 提供了一系列的元素定位方法，常用的有以下几种：

```python
find_element_by_id()  # 通过元素ID定位

find_element_by_name()  # 通过元素Name定位

find_element_by_class_name()  # 通过类名定位

find_element_by_tag_name()  # 通过元素TagName定位

find_element_by_link_text()  # 通过文本内容定位

find_element_by_partial_link_text()

find_element_by_xpath()  # 通过Xpath语法定位

find_element_by_css_selector()  # 通过选择器定位
```

注意:

1、find_element_by_xxx找的是第一个符合条件的标签，find_elements_by_xxx找的是所有符合条件的标签。

2、根据ID、CSS选择器和XPath获取，它们返回的结果完全一致。

3、另外，Selenium还提供了通用方法`find_element()`，它需要传入两个参数：查找方式`By`和值。实际上，它就是`find_element_by_id()`这种方法的通用函数版本，比如`find_element_by_id(id)`就等价于`find_element(By.ID, id)`，二者得到的结果完全一致。

#### 六、节点交互

Selenium可以驱动浏览器来执行一些操作，也就是说可以让浏览器模拟执行一些动作。比较常见的用法有：输入文字时用`send_keys()`方法，清空文字时用`clear()`方法，点击按钮时用`click()`方法。示例如下：

```python
from selenium import webdriver
from time import sleep

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('MAC')  # 输入框接收内容
sleep(1)

input.clear()  # 清空输入框
input.send_keys('IPhone')
button = browser.find_element_by_class_name('btn-search')
button.click()  # 点击按钮
browser.quit()
```

#### 七、动作链

在上面的实例中，一些交互动作都是针对某个节点执行的。比如，对于输入框，我们就调用它的输入文字和清空文字方法；对于按钮，就调用它的点击方法。其实，还有另外一些操作，它们没有特定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。

　　比如，现在实现一个节点的拖曳操作，将某个节点从一处拖曳到另外一处，可以这样实现：

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep


# 创建一个浏览器对象
bro = webdriver.Chrome(executable_path="chromedriver.exe")
# 发起url请求
bro.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

# 定位的标签是存在于iframe的子页面中，如果直接使用find做定位，是定位不到的
# 定位iframe中标签操作
# 第一步：定位到iframe标签位置
bro.switch_to.frame("iframeResult")
# 第二步：通过ID定位到需要拖动的标签
target_ele = bro.find_element_by_id("draggable")


# 创建一个拖动对象
action = ActionChains(bro)
# 点击拖动对象并长按保持
action.click_and_hold(target_ele)

# 模拟拖动5次，每次拖动17个像素点
for i in range(5):
    # 执行拖动动作
    action.move_by_offset(17, 0).perform()
    # 每拖动17像素暂停5秒
    sleep(2)

# 释放拖动对象句柄
action.release()

sleep(2)
# 关闭浏览器
bro.quit()
```

#### 八、执行JavaScript

对于某些操作，Selenium API并没有提供。比如，下拉进度条，它可以直接模拟运行JavaScript，此时使用`execute_script()`方法即可实现，代码如下：

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
# 创建一个浏览器对象
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('https://www.jd.com/')
# 滑动鼠标到下一屏
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 竖直滑动，scrollHeight一屏高度
browser.execute_script('alert("123")')  # js代码，提示框
```

#### 九、获取页面源码数据

通过`page_source`属性可以获取网页的源代码，接着就可以使用解析库（如正则表达式、Beautiful Soup、pyquery等）来提取信息了。

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

# 创建一个浏览器对象
bro = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# 发起url请求
bro.get("http://www.jd.com/")
# 获取网页源码
page_text = bro.page_source
with open("jd.html", "w", encoding="utf-8") as fp:
    fp.write(page_text)
sleep(2)
# 关闭浏览器
bro.quit()
```

#### 十、前进和后退

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
# 创建一个浏览器对象
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# 发起url请求
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('http://www.sina.com.cn/')

browser.back()  # 后退到前一个访问页面
sleep(10)
browser.forward()  # 前进到前一个访问页面
browser.close()
```

#### 十一、标签属性

```python
from selenium import webdriver
# 创建chrome浏览器对象
bro = webdriver.Chrome(executable_path="chromedriver.exe")

# 获取点击按钮的title属性的值
next_page = bro.find_element_by_id("pageIto_next").get_attribute("title")
```

#### 十二、窗口句柄切换

```python
# 获取所有窗口句柄
all_h = dri.window_handles
print(all_h)

# 切换最后窗口句柄
dri.switch_to.window(all_h[-1])

# 切换第一个窗口句柄
dri.switch_to.window(all_h[0])
# 查看当前窗口句柄 print(dri.current_window_handle)
```

#### 十三、Cookie处理

使用Selenium，还可以方便地对Cookies进行操作，例如获取、添加、删除Cookies等。示例如下：

```python
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())  # 获取当前cookie信息

# 添加cookie信息
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())

# 删除所有cookie信息
browser.delete_all_cookies()
print(browser.get_cookies())
```

#### 十四、异常处理

```python
#现在这个比较重要的
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException,NoSuchFrameException

try:
    browser=webdriver.Chrome()
    browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    browser.switch_to.frame('iframssseResult')

except TimeoutException as e:
    print(e)
except NoSuchFrameException as e:
    print(e)
finally:
    browser.close()
```

#### 十五、selenium规避被检测识别

现在不少大网站有对selenium采取了监测机制。比如正常情况下我们用浏览器访问淘宝等网站的 window.navigator.webdriver的值为 
undefined。而使用selenium访问则该值为true。那么如何解决这个问题呢？

　　只需要设置Chromedriver的启动参数即可解决问题。在启动Chromedriver之前，为Chrome开启实验性功能参数`excludeSwitches`，它的值为`['enable-automation']`，完整代码如下：

```python
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)
```

#### 十六、项目实例（selenium站长素材高清图片下载）

```python
from selenium import webdriver
from time import sleep

base_url = "http://sc.chinaz.com/tupian/weimeiyijingtupian.html"

# 创建一个浏览器句柄对象
dri = webdriver.Chrome(executable_path="chromedriver.exe")

# 跳转到指定url
dri.get(base_url)

# 点击跳转图片详情页
dri.find_element_by_xpath('//*[@id="container"]/div[1]/p/a').click()

# 获取所有窗口句柄
all_h = dri.window_handles
print(all_h)

# 切换到新窗口句柄
dri.switch_to.window(all_h[1])

# 查看当前窗口句柄
print(dri.current_window_handle)

sleep(2)

# 点击下载图片(方式一)
# btn = dri.find_element_by_xpath('/html/body/div[7]/div[5]/div[1]/div[6]/div[2]/div[1]/div/div[3]/a[2]')
# btn.click()

# xpath获取所有满足条件的结果，返回一个复数形式(列表)方式二
# btn = dri.find_elements_by_xpath('/html/body/div[5]/div[5]/div[1]/div[6]/div[2]/div[1]/div/div[3]/a[1]')
# print(btn)
# 网速慢可能拿不到结果，可以做异常捕获
# btn[0].click()

# 通过文本信息定位(方式三)
dri.find_element_by_link_text("广东电信下载").click()

sleep(1)
# 退出浏览器
```

#### 十七、项目实例（selenium药监局企业名称获取）

```python
from selenium import webdriver
from time import sleep
import requests

# ajax请求post获取企业详细内容
detail_url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36"
}

# 创建chrome浏览器对象
bro = webdriver.Chrome(executable_path="chromedriver.exe")

# 请求url，请求药监局主页面
bro.get("http://125.35.6.84:81/xk/")

# 定义一个列表：存放所有企业名
title_list = []


# 获取当前页的所有公司的名字
def get_company_title(json_data):
    data_list = json_data["list"]
    for data in data_list:
        title = data['EPS_NAME']
        title_list.append(title)

    return title_list


# 初始psge=1 获取第一页内容
page = 1


# post请求参数
def get_data(page):
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }

    return data


# 请求首页信息
page_text = requests.post(url=detail_url, data=get_data(page), headers=headers).json()

# 首页的公司名字
get_company_title(page_text)
print("获取第1页数据！！！")

# 循环获取其他页信息
for page in range(10):
    # 定位到点击下一页按钮
    next_btn = bro.find_element_by_id("pageIto_next")
    # 点击下一页
    next_btn.click()
    # 延时2秒
    sleep(2)
    # 获取点击按钮的title值
    next_page = bro.find_element_by_id("pageIto_next").get_attribute("title")
    page_text = requests.post(url=detail_url, data=get_data(next_page), headers=headers).json()
    get_company_title(page_text)
    print("获取第{}页数据！！！".format(next_page))


# 打印获取的所有企业名字信息
print(title_list)

sleep(2)
# 关闭浏览器
bro.quit()
```

#### 十八、selenium模拟登录qq空间，爬取数据

```python
import requests
from selenium import webdriver
from lxml import etree
import time

driver = webdriver.Chrome(executable_path='/Users/bobo/Desktop/chromedriver')
driver.get('https://qzone.qq.com/')
#在web 应用中经常会遇到frame 嵌套页面的应用，使用WebDriver 每次只能在一个页面上识别元素，对于frame 嵌套内的页面上的元素，直接定位是定位是定位不到的。
这个时候就需要通过switch_to_frame()方法将当前定位的主体切换了frame 里。
driver.switch_to.frame('login_frame') #login_frame 是ID值
driver.find_element_by_id('switcher_plogin').click()

#driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('328410948')  #这里填写你的QQ号
#driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('xxxxxx')  #这里填写你的QQ密码
    
driver.find_element_by_id('login_button').click()
time.sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
page_text = driver.page_source

tree = etree.HTML(page_text)
#执行解析操作
li_list = tree.xpath('//ul[@id="feed_friend_list"]/li')
for li in li_list:
    text_list = li.xpath('.//div[@class="f-info"]//text()|.//div[@class="f-info qz_info_cut"]//text()')
    text = ''.join(text_list)
    print(text+'\n\n\n')
    
driver.close()
```

> selenium常见的问题及解决办法

> 1、selenium自动化测试时，chrome 出现“Chrome 正受到自动测试软件的控制”的解决办法

`一、在浏览器配置里加个参数，忽略掉这个警告提示语：disable_infobars`使用该方法，浏览器不会弹出'Chrome正在受到自动软件的控制'提示。代码如下：

```python
from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
#return webdriver.Chrome(options = option,desired_capabilities = None)

# 打开chrome浏览器
driver = webdriver.Chrome(options=option)
driver.get("https://www.baidu.com")

##以上的disable-infobars在新版本中失效了，可以采用以下的方法
chrome_options = webdriver.ChromeOptions();

chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

driver = webdriver.Chrome(options=chrome_options);
```

> 2、driver = webdriver.Chrome()这样直接调用而不需要写路径参数r'webdriver路径'

将webdriver.exe文件放到`当前环境Script`文件夹中。

> 3、启动浏览器并加载浏览器的静默模式，让它在后台运行。用 headless

仍有‘Chrome正在受到自动软件的控制’提示，但不影响程序运行。

```python
from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('headless')

# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.baidu.com")
```

> 4、打开谷歌浏览器提示：data，然后自动关闭

下载与Chrome版本匹配的webdriver，浏览器版本与chromeDriver一致，但是打开谷歌仍然提示data;
出现这种情况，其实只要把chromeDriver的位置从python的安装目录复制到Scripts中就可以了。

