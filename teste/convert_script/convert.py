import cv2

img = cv2.imread("images/mclaren.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (200, 200))
cv2.imwrite("mclaren.pgm", img, [cv2.IMWRITE_PXM_BINARY, 0])