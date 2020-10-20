import cv2 as cv
import numpy as np


def empty(a):
    pass


cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)
cv.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 255, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

cap = cv.VideoCapture(0)

while True:
    success, image = cap.read()
    height, width = image.shape[:2]
    image = cv.resize(
        image, (width - (width * 20 // 100), (height - (height * 20 // 100)))
    )
    imgHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    image_result = cv.bitwise_and(image, image, mask=mask)
    print(lower, upper)
    cv.imshow("HSV Image", imgHSV)
    cv.imshow("Original", image)
    cv.imshow("Mask", mask)
    cv.imshow("Result", image_result)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
