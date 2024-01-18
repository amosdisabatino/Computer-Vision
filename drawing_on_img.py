import cv2 as cv

# Drawing on images

img = cv.imread('car2.jpg', cv.IMREAD_COLOR)
img_cut = cv.imread('car2.jpg', cv.IMREAD_COLOR)
img_copy = cv.imread('car2.jpg', cv.IMREAD_COLOR)
cv.line(img, (50, 50), (250, 250), (255, 255, 0), 15)
cv.rectangle(img, (350, 450), (500, 350), (0, 255, 0), 5)
cv. circle(img, (500, 200), 100, (255, 0, 0), 7)

cv.imshow('Car', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Copying Elements

# Replace pixels of the photo with black pixels
img_cut[0:200, 0:300] = [0, 0, 0]

cv.imshow('Car Cut', img_cut)
cv.waitKey(0)
cv.destroyAllWindows()

# Replace pixels of the photo with other pixels of the same photo
copypart = img_copy[0:200, 0:300]
img_copy[200:400, 300:600] = copypart
img_copy[0:200, 0:300] = [0, 0, 0]

cv.imshow('Car Copy Part', img_copy)
cv.waitKey(0)
cv.destroyAllWindows()

# Saving Images

cv.imwrite('car_new.jpg', img_copy)

# Saving Videos

capture = cv.VideoCapture(0)
# `fourcc`, encode video and it specifies the format.
fourcc = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter('video.avi', fourcc, 60.0, (640, 480))

while True:
    ret, frame = capture.read()
    flip_frame = cv.flip(frame, 99889)
    writer.write(flip_frame)
    cv.imshow('Cam', flip_frame)
    if cv.waitKey(1) == ord('x'):
        break

capture.release()
writer.release()
cv.destroyAllWindows()
