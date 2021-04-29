#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 21:06
# @Author  : Ryu
# @Site    : 
# @File    : diff_kernel_affect.py.py
# @Software: PyCharm

import numpy as np
import cv2 as cv
import copy
import util

# 读取图像
origin_img = cv.imread("../img/mission1/car.jpg")
origin_img = copy.copy(origin_img)
origin_gray = cv.cvtColor(origin_img, cv.COLOR_BGR2GRAY)
origin_gray = origin_gray.astype(np.float) / 256
cv.imshow("Raw Gray", origin_gray)
kernel_size = (3, 3)

gauss_img = util.filter(origin_gray, util.Gauss_kernel)
cv.imshow("Gauss Gradient", gauss_img)

center_8_img = util.filter(origin_gray, util.Center_8_kernel)
cv.imshow("Center_8 Gradient", center_8_img)

center_4_img = util.filter(origin_gray, util.Center_4_kernel)
cv.imshow("Center_4 Gradient", center_4_img)

dignoal_img = util.filter(origin_gray, util.Diagonal_opposite_kernel)
cv.imshow("Dignoal Gradient", dignoal_img)

center_peek_img = util.filter(origin_gray, util.Center_peek_kernel)
cv.imshow("Center Peek Gradient", center_peek_img)

origin_kernel_img = util.filter(origin_gray, util.Origin_kernel)
cv.imshow("Origin Gradient", origin_kernel_img)

cv.waitKey(0)
