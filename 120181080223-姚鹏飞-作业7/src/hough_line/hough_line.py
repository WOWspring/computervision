#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/4/27 21:20
#  @Author  : Ryu
#  @Site    :
#  @File    : hough_line.py
#  @Software: PyCharm


import cv2
import numpy as np
import math
import skimage.transform as st


# load img
def detect_line(route):
    line_img = cv2.imread(route)
    line_img = np.copy(line_img)
    line_img_copy = cv2.cvtColor(line_img, cv2.COLOR_BGR2RGB)
    line_img_gray = cv2.cvtColor(line_img_copy, cv2.COLOR_RGB2GRAY)

    # detect edge
    line_edges = cv2.Canny(line_img_gray, 50, 100)
    cv2.imshow("edge", line_edges)
    # hough transform
    h, angles, d = st.hough_line(line_edges)
    lines = cv2.HoughLines(line_edges, 1, np.pi / 180, 100)

    img_h = np.copy(line_img_copy)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img_h, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return np.log(1 + h), img_h

def detect_line_p(route):
    line_img = cv2.imread(route)
    line_img = np.copy(line_img)
    line_img_copy = cv2.cvtColor(line_img, cv2.COLOR_BGR2RGB)
    line_img_gray = cv2.cvtColor(line_img_copy, cv2.COLOR_RGB2GRAY)

    # detect edge
    line_edges = cv2.Canny(line_img_gray, 100, 120)
    cv2.imshow("edge", line_edges)
    # hough transform
    h, angles, d = st.hough_line(line_edges)
    lines = cv2.HoughLines(line_edges, 1, np.pi / 180, 180)

    img_h = np.copy(line_img_copy)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img_h, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return np.log(1 + h), img_h

# cv2.imshow("h", np.log(1 + h))


# cv2.waitKey(0)

if __name__ == '__main__':
    # img1_route = r"../../img/hough_line/image001.png"
    # h1, img1 = detect_line(img1_route)
    # cv2.imshow("img1_peak", h1)
    # cv2.imshow("img1_detected", img1)
    #
    # img2_route = r"../../img/hough_line/image002.png"
    # h2, img2 = detect_line(img2_route)
    # cv2.imshow("img2_peak", h2)
    # cv2.imshow("img2_detected", img2)

    img3_route = r"../../img/hough_line/image003.png"
    h3, img3 = detect_line_p(img3_route)
    # cv2.imshow("img3_peak", h3)
    cv2.imshow("img3_detected", img3)

    cv2.waitKey(0)
