import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    _, img = camera.read()
    flip_img = cv.flip(img, 1)
    hsv = cv.cvtColor(flip_img, cv.COLOR_RGB2HSV)
    min = np.array([100, 60, 0])
    max = np.array([255, 255, 255])
    mask = cv.inRange(hsv, min, max)

    median = cv.medianBlur(mask, 15)
    median = cv.bitwise_and(flip_img, flip_img, mask=median)

    cv.imshow('Median', median)

    if cv.waitKey(5) == ord('x'):
        break

cv.destroyAllWindows()
camera.release()
