import cv2

img = cv2.imread('002476.jpg')

img1 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

cv2.imshow('11', img1)

cv2.waitKey(0)