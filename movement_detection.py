import cv2 as cv

video = cv.VideoCapture(0)
subtractor = cv.createBackgroundSubtractorMOG2(20, 50)

while True:
    _, frame = video.read()
    mask = subtractor.apply(frame)
    cv.imshow('Mask', mask)
    if cv.waitKey(5) == ord('x'):
        break

cv.destroyAllWindows()
video.release()
