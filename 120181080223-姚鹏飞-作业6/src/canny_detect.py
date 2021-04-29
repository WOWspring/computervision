#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 22:07
# @Author  : Ryu
# @Site    : 
# @File    : canny_detect.py
# @Software: PyCharm

import cv2 as cv
import numpy as np
import copy

origin_img = cv.imread("../img/mission2/flower.jpg")
origin_img = copy.copy(origin_img)
origin_gray = cv.cvtColor(origin_img, cv.COLOR_BGR2GRAY)
# cv.imshow("Origin", origin_gray)

edges_img = cv.Canny(origin_gray, threshold1=100, threshold2=200, apertureSize=3, L2gradient=False)
cv.imshow("Edges", edges_img)

cv.waitKey(0)

