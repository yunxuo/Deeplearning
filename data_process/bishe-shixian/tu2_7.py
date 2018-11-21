import cv2


img = cv2.imread('E:\deeplearning\Image\pascal\JPEGImages\JPEGImages//000001.jpg')
cv2.rectangle(img,(166,127),(290,185),(0,255,0),2)

cv2.imshow('aa',img)
cv2.waitKey(0)