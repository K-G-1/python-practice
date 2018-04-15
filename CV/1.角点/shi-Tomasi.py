#coding=utf-8

import numpy as np
import cv2

img = cv2.imread('car-4.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 输出最多50个角点 qualityLevel为0.01 角点间最小距离为50
cornerPoints = cv2.goodFeaturesToTrack(grayImg, 100, 0.01, 1)
cornerPoints = np.int0(cornerPoints)

for i in cornerPoints:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, [0, 0, 255], -1)

print((cornerPoints.shape))
cv2.imshow('Shi-Tomasi', img)
cv2.imshow("gray",grayImg)
cv2.waitKey()