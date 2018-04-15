#coding=utf-8

import cv2
import numpy as np

img = cv2.imread('car-4.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayImg = np.float32(grayImg)
harriImg = cv2.cornerHarris(grayImg, 2, 3, 0.04)
# 膨胀运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
harriImgD = cv2.dilate(harriImg, kernel)
# 设置阈值 实际是对Harri的输出矩阵进行过滤 而输出矩阵又可以用图像形象的表现
img[harriImgD > 0.05*harriImgD.max()] = [0, 0, 255]
cv2.imshow('Harri', harriImgD)
cv2.imshow('Output', img)

cv2.waitKey()
cv2.destroyAllWindows()