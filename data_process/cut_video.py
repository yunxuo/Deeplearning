import cv2

cap = cv2.VideoCapture('C:/Users/yunxu/Desktop/Video_2018-05-02_135220.wmv')

h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

s = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

print()