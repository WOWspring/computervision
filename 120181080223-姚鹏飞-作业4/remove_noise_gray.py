#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/4/3 21:25
#  @Author  : Ryu
#  @Site    :
#  @File    : remove_noise_gray.py
#  @Software: PyCharm

import cv2 as cv
import numpy as np


def read_img(dir_img):
    img = cv.imread(dir_img)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img


def add_noise(img, mean=0, sigma=0.05):
    img = np.array(img / 255, dtype=float)
    img = cv.resize(img, dsize=(img.shape[0] // 3 * 2, img.shape[1] // 3 * 2))
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
    img = read_img(dir)
    img = add_noise(img)
    print("KernelSize的对比")
    sigma_x = 1
    filter3 = cv.GaussianBlur(img, ksize=(3, 3), sigmaX=sigma_x)
    cv.imshow("3x3FilterWithSigma1", filter3)
    # cv.waitKey(0)
    filter5 = cv.GaussianBlur(img, ksize=(5, 5), sigmaX=sigma_x)
    cv.imshow("5x5ilterWithSigma1", filter5)
    # cv.waitKey(0)
    filter7 = cv.GaussianBlur(img, ksize=(7, 7), sigmaX=sigma_x)
    cv.imshow("7x7ilterWithSigma1", filter7)
    cv.waitKey(0)


    cv.imshow("Gauss", img)
    sigma_x = 2
    filter3 = cv.GaussianBlur(img, ksize=(3, 3), sigmaX=sigma_x)
    cv.imshow("3x3FilterWithSigma2", filter3)
    # cv.waitKey(0)
    filter5 = cv.GaussianBlur(img, ksize=(5, 5), sigmaX=sigma_x)
    cv.imshow("5x5FilterWithSigma2", filter5)
    # cv.waitKey(0)
    filter7 = cv.GaussianBlur(img, ksize=(7, 7), sigmaX=sigma_x)
    cv.imshow("7x7FilterWithSigma2", filter7)
    cv.waitKey(0)

    print("Sigma对比")
    cv.imshow("Gauss", img)
    kernel_size = (3,3)
    sigma1 = cv.GaussianBlur(img, kernel_size, sigmaX=0.5)
    cv.imshow("3x3FilterWithSigma0.5", sigma1)
    sigma2 = cv.GaussianBlur(img, kernel_size, sigmaX=1)
    cv.imshow("3x3FilterWithSigma1", sigma2)
    sigma3 = cv.GaussianBlur(img, kernel_size, sigmaX=1.5)
    cv.imshow("3x3FilterWithSigma1.5", sigma3)
    cv.waitKey(0)

    kernel_size = (5, 5)
    cv.imshow("Gauss", img)
    sigma4 = cv.GaussianBlur(img, kernel_size, sigmaX=0.5)
    cv.imshow("5x5FilterWithSigma0.5", sigma4)
    sigma5 = cv.GaussianBlur(img, kernel_size, sigmaX=1)
    cv.imshow("5x5FilterWithSigma1", sigma5)
    sigma6 = cv.GaussianBlur(img, kernel_size, sigmaX=1.5)
    cv.imshow("5x5FilterWithSigma1.5", sigma6)
    cv.waitKey(0)