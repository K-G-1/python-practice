# coding=utf-8

import cv2
import numpy as np
import time 


cap = cv2.VideoCapture(0)

# 定义fourecc代码
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 创建VideoWriter对象
out = cv2.VideoWriter('output.avi',fourcc, 60.0, (640,480))

print cap.isOpened()
while True:
    now = time.time()
    # print cap.isOpened()
    # cv2.waitKey(100)
    if cap.isOpened():
        ret, frame = cap.read()
        out.write(frame)
        # cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF is ord('q'):
            break


cap.release()
out.release()
cv2.destroyAllWindows()
