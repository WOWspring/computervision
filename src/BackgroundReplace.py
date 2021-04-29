#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/3/13 10:32
#  @Author  : Wowspring
#  @Site    :
#  @File    : BackgroundReplace.py
#  @Software: PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread("../img/certificate.jpg")
image = np.copy(image)
print('this image is:', type(image), 'with dimensions:', image.shape)

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.show()
lower_gray = np.array(235)
upper_gray = np.array(255)

mask = cv2.inRange(gray_image, lower_gray, upper_gray)
plt.imshow(mask, cmap='gray')
plt.show()

# 腐蚀膨胀
erode = cv2.erode(mask, None, iterations=1)
# plt.imshow(erode)
# plt.show()
dilate = cv2.dilate(erode, None, iterations=1)
# plt.imshow(dilate)
# plt.show()
masked_img = np.copy(image)
masked_img[dilate != 0] = [0, 0, 0]
plt.imshow(masked_img)
plt.show()

# Background img
background_image = mpimg.imread('../img/sky2.jpeg')
crop_background_image = background_image[0:masked_img.shape[0], 0:masked_img.shape[1]]
plt.imshow(crop_background_image)
print('Image dimensions:', crop_background_image.shape)
plt.show()

crop_background = np.copy(crop_background_image)
crop_background[dilate == 0] = [0, 0, 0]
plt.imshow(crop_background)
plt.show()

print('Masked Image dimensions:', masked_img.shape)
print('background Image dimensions:', crop_background.shape)

complete_image = masked_img + crop_background
plt.imshow(complete_image)
plt.show()

mpimg.imsave('../img/certificateandsky.jpg', complete_image)
