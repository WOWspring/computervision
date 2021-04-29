#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/3/24 20:41
#  @Author  : Ryu
#  @Site    :
#  @File    : classification.py
#  @Software: PyCharm

import cv2
import helpers
import numpy as np
import random


def avg_brightness(rgb_image):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    sum_brightness = np.sum(hsv[:, :, 2])
    w, h, _ = rgb_image.shape
    area = w * h
    avg = sum_brightness / area
    return avg


def estimate_label(rgb_image, threshold=120):
    # w, h, _ = rgb_image.shape
    target_list = split_image(rgb_image)
    avg_list = []
    for i in target_list:
        avg_list.append(avg_brightness(i))
    if vote(avg_list, threshold):
        return 1
    else:
        return 0


def split_image(rgb_image, split_num=(5, 5)):
    splited_img_list = []
    w, h, _ = rgb_image.shape
    split_w = int(w // split_num[0])
    split_h = int(h // split_num[1])
    for i in range(split_num[0]):
        for j in range(split_num[1]):
            temp = rgb_image[split_w * i: split_w * (i + 1), split_h * j: split_h * (j + 1), :]
            splited_img_list.append(temp)
    return splited_img_list


def vote(avg_list, threshold=120):
    vote = 0
    for avg_score in avg_list:
        if avg_score > threshold:
            vote += 1
    return True if vote > 10 else False


def get_misclassified_images(test_images, threshold=120):
    misclassified_images_labels = []
    for image in test_images:
        im = image[0]
        true_label = image[1]
        predicted_label = estimate_label(im, threshold)
        if predicted_label != true_label:
            misclassified_images_labels.append((im, predicted_label, true_label))
    return misclassified_images_labels


def visualize_img():
    for i in MISCLASSIFIED:
        test_mis_im = i[0]
        cv2.imshow("misclassified", test_mis_im)
        print(str(i[1]))
        cv2.waitKey()


def auto_judge(epochs, init_lr=16, threshold=120):
    post_flag = 0
    thr = threshold
    learning_rate = init_lr
    max_accuracy = 0
    last_accuracy = 0
    best_threshold = threshold
    for i in range(epochs):
        thr = thr + learning_rate if post_flag == 1 else thr - learning_rate
        temp_accuracy = get_accuracy(thr)
        print("when threshold is " + str(thr) + ", accuracy is " + str(temp_accuracy))
        if temp_accuracy > max_accuracy:
            max_accuracy = temp_accuracy
            best_threshold = thr
        else:
            if temp_accuracy <= last_accuracy:
                post_flag = 1 if post_flag == 0 else 0
            learning_rate /= 2.
        last_accuracy = temp_accuracy
    return best_threshold, max_accuracy


def get_accuracy(threshold=120):
    MISCLASSIFIED = get_misclassified_images(STANDARDIZED_TEST_LIST, threshold)
    total = len(STANDARDIZED_TEST_LIST)
    num_correct = total - len(MISCLASSIFIED)
    accuracy = num_correct / total
    return accuracy


if __name__ == '__main__':
    image_dir_training = "day_night_images/training/"
    image_dir_test = "day_night_images/test/"
    TEST_IMAGE_LIST = helpers.load_dataset(image_dir_test)
    STANDARDIZED_TEST_LIST = helpers.standardize(TEST_IMAGE_LIST)
    random.shuffle(STANDARDIZED_TEST_LIST)
    MISCLASSIFIED = []
    auto_judge(epochs=10)
