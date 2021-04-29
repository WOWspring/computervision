#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/4/13 20:52
#  @Author  : Ryu
#  @Site    :
#  @File    : util.py
#  @Software: PyCharm

import cv2 as cv
import numpy as np

Gauss_kernel = np.array([[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]], dtype=np.float)

Center_8_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float)

Center_4_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float)

Diagonal_opposite_kernel = np.array([[-2, -1, 0], [-1, 1, -1], [0, 1, 2]], dtype=np.float)

Center_peek_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float)

Origin_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.float)

sobel_kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float)

sobel_kernel_x_reverse = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], dtype=np.float)

sobel_kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float)

sobel_kernel_y_reverse = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float)

kernel_size = (3, 3)


def filter(origin_gray, kernel):
    gradient_img = np.zeros((origin_gray.shape[0] - kernel_size[0] + 1, origin_gray.shape[1] - kernel_size[1] + 1),
                            dtype=np.float)
    for i in range(gradient_img.shape[0]):
        for j in range(gradient_img.shape[1]):
            gradient_img[i][j] = np.sum(
                np.multiply(kernel, origin_gray[i:i + kernel_size[0], j:j + kernel_size[1]]))
    return gradient_img



def threshold_demo(gray):
    #直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    # print("threshold value %s"%ret)
    cv.namedWindow("binary0", cv.WINDOW_NORMAL)
    cv.imshow("binary0", binary)