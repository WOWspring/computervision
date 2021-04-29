#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/4/13 22:17
#  @Author  : Ryu
#  @Site    :
#  @File    : find_password.py
#  @Software: PyCharm

import cv2 as cv
import numpy as np
import copy
import util
car_img = cv.imread("../img/mission3/car.jpg")
joker_img = cv.imread("../img/mission3/joker.jpg")

car_img = copy.copy(car_img)
joker_img = copy.copy(joker_img)
car_gray = cv.cvtColor(car_img, cv.COLOR_BGR2GRAY)
joker_gray = cv.cvtColor(joker_img, cv.COLOR_BGR2GRAY)

# cv.imshow("Origin", origin_gray)

# # edges_car = cv.Sobel(car_gray, ddepth=-1, dx=0, dy=1, ksize=3)
# edges_car = util.filter(car_gray, util.sobel_kernel_y_reverse)
#
# rat, edges_car = cv.threshold(edges_car, 80, 255, type=cv.THRESH_BINARY)
# # edges_joker = cv.Sobel(joker_gray, ddepth=-1, dx=1, dy=0, ksize=3)
# edges_joker = util.filter(joker_gray, util.sobel_kernel_x_reverse)
# # edges_joker_flip = cv.flip(edges_joker, 1)
# # edges_joker = edges_joker + edges_joker_flip
# rat, edges_joker = cv.threshold(edges_joker, 80, 255, type=cv.THRESH_BINARY)
# edges_mixed = (edges_joker + edges_car) / 2
# cv.imshow("Car Edges", edges_car)
# cv.imshow("Jkoer Edges", edges_joker)
# cv.imshow("Mixed Edges", edges_mixed)


edges_car = cv.Canny(car_gray, threshold1=20, threshold2=100, apertureSize=3, L2gradient=False)
# cv.imshow("car1", edges_car)
rat, edges_car = cv.threshold(edges_car, 80, 255, type=cv.THRESH_BINARY)
# cv.imshow("car2", edges_car)

edges_joker = cv.Canny(joker_gray, threshold1=100, threshold2=200, apertureSize=3, L2gradient=False)
rat, edges_joker = cv.threshold(edges_joker, 80, 255, type=cv.THRESH_BINARY)
edge_mixed = edges_joker & edges_car
cv.imshow("car", edges_car)
cv.imshow("joker", edges_joker)
cv.imshow("and operation", edge_mixed)



# 边缘连接
def edge_connection(img, size, k):
    for i in range(size):
        Yi = np.where(img[i, :] > 0)
        if len(Yi[0]) >= 100:
            for j in range(0, len(Yi[0])-1):
                if Yi[0][j+1] - Yi[0][j] <= k:
                    img[i, Yi[0][j]:Yi[0][j+1]] = 1
    return img

edge_mixed = edge_connection(edge_mixed, edge_mixed.shape[0], k = 10)
edge_mixed = cv.rotate(edge_mixed, 0)
edge_mixed = edge_connection(edge_mixed, edge_mixed.shape[0], k = 10)
edge_mixed = cv.rotate(edge_mixed, 0)
edge_mixed = cv.rotate(edge_mixed, 0)
edge_mixed = cv.rotate(edge_mixed, 0)

cv.imshow("connection", edge_mixed)

cv.waitKey(0)
