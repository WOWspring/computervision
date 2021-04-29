#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/4/10 23:35
#  @Author  : Ryu
#  @Site    :
#  @File    : correlation.py.py
#  @Software: PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import copy
import math

origin = cv.imread("images/origin.jpg")
origin = copy.copy(origin)

template = cv.imread("images/template.jpg")
template = copy.copy(template)

origin_gray = cv.cvtColor(origin, cv.COLOR_BGR2GRAY)
origin_gray = origin_gray.astype(np.float) / 256
template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
template_gray = template_gray.astype(np.float) / 256

pointx = 0
pointy = 0
max_inf = -1.0
find = np.zeros((origin.shape[0] - template.shape[0] + 1, origin.shape[1] - template.shape[1] + 1), dtype=np.float)

# 平方差
# for i in range(find.shape[0]):
#     for j in range(find.shape[1]):
#         find[i][j] = np.sum((template_gray - origin_gray[i:i + template.shape[0], j:j + template.shape[1]]) ** 2)
#         if (find[i][j] < max_inf):
#             max_inf = find[i][j]
#             pointx = i
#             pointy = j

# 相关系数匹配
num = template_gray.shape[0] * template_gray.shape[1]
template_gray_mean = np.mean(template_gray)
template_gray_submean = template_gray - template_gray_mean
sigma_template = math.sqrt(1. / (num - 1) * np.sum(template_gray_submean ** 2))

for i in range(find.shape[0]):
    for j in range(find.shape[1]):
        origin_patch = origin_gray[i:i + template_gray.shape[0], j:j + template_gray.shape[1]]
        origin_patch_mean = np.mean(origin_patch)
        origin_patch_submean = origin_patch - origin_patch_mean
        cov = 1. / (num - 1) * np.sum(np.multiply(origin_patch_submean, template_gray_submean))
        sigma_origin_patch = math.sqrt(1. / (num - 1) * np.sum(origin_patch_submean ** 2))
        coefficient = cov / (sigma_origin_patch * sigma_template)

        find[i][j] = coefficient
        if (find[i][j] > max_inf):
            max_inf = find[i][j]
            pointx = i
            pointy = j

# 相关匹配
# for i in range(find.shape[0]):
#     for j in range(find.shape[1]):
#         find[i][j] = np.sum(np.multiply(template_gray, origin_gray[i:i + template_gray.shape[0], j:j + template_gray.shape[1]]))
#         if (find[i][j] > max_inf):
#             max_inf = find[i][j]
#             pointx = i
#             pointy = j
# find = find.astype(np.float)
# print(find)

cv.circle(find, (pointy, pointx), 10, (255, 255, 255), 3)
cv.rectangle(origin, (pointy, pointx), (pointy + template.shape[1], pointx + template.shape[0]), (0, 0, 255), 5)

cv.imshow("find", find)
cv.imshow('original image', origin)
cv.waitKey(0)
