import cv2 as cv

# Pre-trained machine learning model via 'Haar' algorithm.
faces_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv.VideoCapture(0)

while True:
    _, frame = video.read()
    frame = cv.resize(frame, (1400, 900))
    # The face recognition works better with 'gray scale' images.
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    faces = faces_cascade.detectMultiScale(gray, 1.3, 10)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y+h), (255, 0, 0), 2)
        cv.putText(
            frame, 'FACE', (x, y+h+30), cv.FONT_HERSHEY_SIMPLEX, 0.8,
            (255, 255, 255), 2
        )
    cv.imshow('Face', frame)
    if cv.waitKey(5) == ord('x'):
        break

cv.destroyAllWindows()
video.release()
