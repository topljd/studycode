'''
putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)
img：操作的图片数组
text：需要在图片上添加的文字
fontFace：字体风格设置
fontScale：字体大小设置
color：字体颜色设置
thickness：字体粗细设置
'''
import cv2
#加载背景图片
bk_img = cv2.imread(r'C:\Users\ljd\Desktop\001.jpg')
#在图片上添加文字信息
cv2.putText(bk_img,'hello world',(100,300), cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255), 1, cv2.LINE_AA)

#显示图片
cv2.imshow('add_text',bk_img)
cv2.waitKey()

#保存图片
cv2.imwrite('add_text.jpg',bk_img)