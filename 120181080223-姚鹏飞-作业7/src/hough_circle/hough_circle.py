#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/4/28 21:37
#  @Author  : Ryu
#  @Site    :
#  @File    : hough_circle.py
#  @Software: PyCharm

import cv2
import numpy as np


def cvt_img(img):
    copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(copy, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray, 100, 120)
    # cv2.imshow("edge", edges)
    return copy, edges


def cvt_img2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(gray, 10, 20)
    cv2.imshow("edge", edges)
    return img, edges


def circle_detect(route):
    circle_img = cv2.imread(route)
    circle_img = np.copy(circle_img)
    copy, edges = cvt_img2(circle_img)
    i = 0
    if i == 0:
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, minDist=10, param1=100, param2=80, maxRadius=165,
                                   minRadius=120)[0, :, :]
        # circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, minDist=10)[0, :, :]
        circles = np.uint16(np.around(circles))
        for i in circles:
            cv2.circle(copy, (i[0], i[1]), i[2], (0, 0, 255), 2)
    return copy


if __name__ == '__main__':
    route_img1 = r"../../img/hough_circle/coins.png"
    img1 = circle_detect(route_img1)
    cv2.imshow("img1", img1)
    cv2.waitKey(0)
