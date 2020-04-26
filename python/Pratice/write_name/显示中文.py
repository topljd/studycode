import cv2
from PIL import ImageFont,ImageDraw,Image
import numpy as np
bk_img = cv2.imread(r'C:\Users\ljd\Desktop\rongyu.jpg')
#设置需要显示的字体
fontpath = "font/simkai.ttf"
font = ImageFont.truetype(fontpath, 55)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
#绘制文字信息
draw.text((330, 965),  "李子安", font = font, fill = (0, 0, 0))
bk_img = np.array(img_pil)

#cv2.imshow("add_text",bk_img)
#cv2.waitKey()
cv2.imwrite("add_text.jpg",bk_img)