import cv2 as cv
import numpy as np

img = cv.imread('f75.jpg')
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

min = np.array([100, 60, 0])
max = np.array([255, 255, 255])

mask = cv.inRange(hsv, min, max)
result = cv.bitwise_and(img, img, mask=mask)

averages = np.ones((15, 15), np.float32) / 255
smoothed = cv.filter2D(result, -1, averages)

blur = cv.GaussianBlur(result, (15, 15), 0)

median_blur = cv.medianBlur(mask, 15)
result2 = cv.bitwise_and(img, img, mask=median_blur)

cv.imshow('Result', result)
cv.waitKey(0)
cv.imshow('Result Smoothed', smoothed)
cv.waitKey(0)
cv.imshow('Result Gaussian Blur', blur)
cv.waitKey(0)
cv.imshow('Result Median Blur', result2)
cv.waitKey(0)
cv.destroyAllWindows()
