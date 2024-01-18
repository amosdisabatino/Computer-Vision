import cv2 as cv

img1 = cv.imread('car2.jpg')
img2 = cv.imread('logo.jpg')

# Thresholding

logo_gray = cv.cvtColor(img2, cv.COLOR_RGB2GRAY)
ret, mask = cv.threshold(logo_gray, 180, 255, cv.THRESH_BINARY_INV)

mask_inv = cv.bitwise_not(mask)

rows, columns, channels = img2.shape

area = img1[0:rows, 0:columns]

img1_bg = cv.bitwise_and(area, area, mask=mask_inv)
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

result = cv.add(img1_bg, img2_fg)

img1[0:rows, 0:columns] = result

cv.imshow('Result', img1)
cv.waitKey(0)
cv.destroyAllWindows()

book_page = cv.imread('book_page.jpg')
book_page_gray = cv.cvtColor(book_page, cv.COLOR_RGB2GRAY)
gaus = cv.adaptiveThreshold(
    book_page_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81,
    6,
)

cv.imshow('Original Book Page', book_page)
cv.waitKey(0)
cv.imshow('Result Book Page with Gaussian Thresholding', gaus)
cv.waitKey(0)
cv.destroyAllWindows()
