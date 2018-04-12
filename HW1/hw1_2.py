import cv2
import numpy as np
from matplotlib import pyplot as plt


def bgr2yuv(img):
    bgrcolors = cv2.split(img)
    B, G, R = bgrcolors[0], bgrcolors[1], bgrcolors[2]
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    U = - 0.1687 * R - 0.3313 * G + 0.5 * B + 128
    V = 0.5 * R - 0.4187 * G - 0.0813 * B - 128
    yuvcolors = [Y, U, V]
    new_img = cv2.merge(yuvcolors)
    new_img = np.asarray(new_img,dtype=np.uint8)
    return new_img


def yuv2bgr(img):
    yuvcolors = cv2.split(img)
    Y, U, V = yuvcolors[0], yuvcolors[1], yuvcolors[2]
    R = Y + 1.14 * V - 128
    G = Y - 0.39 * U - 0.58 * V - 128
    B = Y + 2.03 * U
    bgrcolors = [B, G, R]
    new_img = cv2.merge(bgrcolors)
    new_img = np.asarray(new_img,dtype=np.uint8)
    return new_img


img = cv2.imread('fudan.jpg')
cv2.imshow("Original Image", img)

img1 = bgr2yuv(img)
cv2.imshow("YUV Image(My own algorithm)", img1)

img1_lib = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow("YUV Image(Using the lib)", img1_lib)

img2 = yuv2bgr(img1)
cv2.imshow("RGB Image", img2)

img2_lib = cv2.cvtColor(img1_lib, cv2.COLOR_YUV2BGR)
cv2.imshow("RGB Image(Using the lib)",img2_lib)