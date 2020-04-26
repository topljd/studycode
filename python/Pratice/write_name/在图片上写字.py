import cv2
from PIL import ImageFont,ImageDraw,Image
import numpy as np
import xlrd
import time
#bk_img = cv2.imread(r'001.jpg')
# #设置需要显示的字体
# fontpath = "font/simkai.ttf"
# font = ImageFont.truetype(fontpath, 55)
# img_pil = Image.fromarray(bk_img)
# draw = ImageDraw.Draw(img_pil)

#读取excel的数据
file_name = r'C:\Users\Administrator\Desktop\0001.xlsx'
file = xlrd.open_workbook(file_name)
# 读取某张表
sheet = file.sheet_by_name("Sheet1")
# 获取第3列的数据
col_value = sheet.col_values(2)
print(col_value)

#解决Python下imread，imwrite不支持中文
def cv_imwrite(filename,src):
    cv2.imencode('.jpg',src)[1].tofile(filename)

def cv_imread(file_path):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img

#这里的范围是表格里面的顺序
for i in range(0,208):
    info = str(i+1)+col_value[i]
    print(info)
    origin_name = col_value[i]
    name_len = len(col_value[i])
    if name_len == 3:
        name = origin_name[0]+' '+origin_name[1]+' '+origin_name[2]
    elif name_len == 4:
        if ' ' not in origin_name:
            name = origin_name
        else:
            name = origin_name[0]+'  '+origin_name[1:]
    else:
        name = origin_name
    #绘制文字信息
    bk_img = cv2.imread(r'208.jpg')
    # 设置需要显示的字体
    fontpath = "font/msyhbd.ttc"
    font = ImageFont.truetype(fontpath, 100)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((660, 1810), name, font = font, fill = (0, 0, 0))
    bk_img = np.array(img_pil)
    #cv2.imshow("add_text",bk_img)
    #cv2.waitKey()
    image_url = "images/"+info+".jpg"
    cv_imwrite(image_url,bk_img)
    time.sleep(0.1)