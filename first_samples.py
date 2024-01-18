import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('car.jpg', cv.IMREAD_COLOR)

# 1- SHOWING IMAGES WITH OPENCV

# We use 'cv.IMREAD_COLOR' because we want to work with the coloured version of
# the image.
cv.imshow('Car', img)
cv.waitKey(0)
cv.destroyAllWindows()

# 2- SHOWING IMAGES WITH MATPLOTLIB

# OpenCV uses the 'RGB' color scheme, Matplotlib uses the 'BGR' color scheme,
# so we need to convert the color scheme with 'cv.COLOR_RGB2BGR'.
img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

plt.imshow(img)
plt.show()

# 3- LOADING VIDEOS OR 'CAMERA DATA'

# 3.1- Loading Videos
video = cv.VideoCapture('sample.mp4')

# 3.2- Loading Camera Data
video = cv.VideoCapture(0)

while True:
    ret, frame = video.read()
    if ret:
        # If we use the 'webcam' data, we can flip the 'image'
        # flip_frame = cv.flip(frame, 1)
        # cv.imshow('Sample Video', flip_frame)
        cv.imshow('Sample Video', frame)
        if cv.waitKey(30) == ord('x'):
            break
    else:
        break

video.release()
cv.destroyAllWindows()
