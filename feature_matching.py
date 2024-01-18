import cv2 as cv

img1 = cv.imread('workspace.jpg')
img2 = cv.imread('workspace2.jpg')

orb = cv.ORB_create()

keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = matcher.match(descriptors1, descriptors2)
matches = sorted(matches, key=lambda x: x.distance)

result = cv.drawMatches(
    img1, keypoints1, img2, keypoints2, matches[:5], None, flags=2)

result = cv.resize(result, (1600, 900))
cv.imshow('Result', result)
cv.waitKey(0)
