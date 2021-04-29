#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/4/4 13:38
#  @Author  : Ryu
#  @Site    :
#  @File    : remove_noise_rgb.py
#  @Software:

import cv2 as cv
import numpy as np


def add_noise(img, mean=0, sigma=0.05):
    img = np.array(img / 255, dtype=float)
    noise = np.random.normal(mean, sigma ** 0.5, img.shape)
    out = img + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    cv.imshow("gasuss", out)
    # cv.waitKey(0)
    return out


if __name__ == '__main__':
    dir = "images\papper.bmp"
    img = cv.imread(dir)
    img = add_noise(img)

    filter3 = cv.GaussianBlur(img, ksize=(5, 5), sigmaX=5./3.)
    cv.imshow("3x3FilterWithSigma1", filter3)
    cv.waitKey(0)
