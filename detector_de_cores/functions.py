import cv2 as cv
import numpy as np


def generate_mask(max_hsv, min_hsv, hsv_image):
    lower = np.array(min_hsv)
    high = np.array(max_hsv)
    mask = cv.inRange(hsv_image, lower, high)

    return mask
