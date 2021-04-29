#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/3/13 14:55
#  @Author  : Ryu
#  @Site    :
#  @File    : VideoBgReplace.py
#  @Software: PyCharm

import cv2
from ReplaceFunc import replace

cap = cv2.VideoCapture("../img/butterfly.flv")
background_img = cv2.imread("../img/sky.jpeg")
background_img = cv2.resize(background_img, (640, 360))

# 视频保存路径
fps = 24
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('../img/butterflyandsky.avi', fourcc, fps, (640, 360), True)

while cap.isOpened():
    ret, frame = cap.read()
    new_img = replace(frame, background_img)
    videoWriter.write(new_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("成功生成视频！")

cap.release()
cv2.destroyAllWindows()
