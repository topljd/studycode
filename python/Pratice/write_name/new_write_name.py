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

#解决Python下imread，imwrite不支持中文
def cv_imwrite(filename,src):
    cv2.imencode('.jpg',src)[1].tofile(filename)

def cv_imread(file_path):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img
info = '李子安'
#绘制文字信息
bk_img = cv2.imread(r'rongyu01.jpg')
# 设置需要显示的字体
fontpath = "font/msyhbd.ttc"
font = ImageFont.truetype(fontpath, 100)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
draw.text((880, 1830), info, font = font, fill = (0, 0, 0))
bk_img = np.array(img_pil)
#cv2.imshow("add_text",bk_img)
#cv2.waitKey()
image_url = "images/"+info+".jpg"
cv_imwrite(image_url,bk_img)