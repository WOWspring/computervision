#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/13 15:10
# @Author  : Ryu
# @Site    : 
# @File    : ReplaceFunc.py
# @Software: PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def replace(frame, background):
    image = np.copy(frame)
    lower_green = np.array([0, 100, 0])
    upper_green = np.array([80, 255, 80])

    mask = cv2.inRange(image, lower_green, upper_green)

    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    dilate = cv2.dilate(erode, None, iterations=1)
    masked_img = np.copy(image)
    masked_img[dilate != 0] = [0, 0, 0]

    # Background img
    background_image = background
    crop_background_image = background_image[0:masked_img.shape[0], 0:masked_img.shape[1]]

    crop_background = np.copy(crop_background_image)
    crop_background[dilate == 0] = [0, 0, 0]

    complete_image = masked_img + crop_background
    return complete_image