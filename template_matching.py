import cv2 as cv
import numpy as np

img_bgr = cv.imread('workspace.jpg')
img_gray = cv.cvtColor(img_bgr, cv.COLOR_RGB2GRAY)

template = cv.imread('key.jpg', 0)
width, height = template.shape[::-1]

result = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

threshold = 0.715
area = np.where(result >= threshold)

for pixel in zip(*area[::-1]):
    cv.rectangle(
        img_bgr, pixel, (pixel[0] + width, pixel[1] + height),
        (0, 0, 255), 2
    )

cv.imshow('Result', img_bgr)
cv.waitKey(0)
cv.destroyAllWindows()
