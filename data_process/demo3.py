import cv2
from PIL import Image
from pylab import *

def drawing(flag, point, id, type, weight,img):
    p1 = (int(point[0])-15, int(point[1])-9)
    p2 = (int(point[0])+15, int(point[1])+9)
    color = (0, 0, 255)
    thick = 1

    cv2.rectangle(img, p1, p2, color, thick)
    if flag == 1:
        cv2.line(img, (int(point[0]), int(point[1])), (int(point[0]), int(point[1] - 140)), (0, 0, 255), 1)
        cv2.putText(img, 'ID:' + str(id), (int(point[0] + 5), int(point[1] - 130)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 255), 1)
        cv2.putText(img, 'TYPE:' + str(type), (int(point[0] + 5), int(point[1] - 115)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 255), 1)
        cv2.putText(img, 'WEIGHT:' + str(weight), (int(point[0] + 5), int(point[1] - 100)), cv2.FONT_HERSHEY_COMPLEX,
                    0.5, (0, 0, 255), 1)
    if flag == 2:
        cv2.line(img, (int(point[0]), int(point[1])), (int(point[0]), int(point[1] - 110)), (0, 0, 255), 1)
        cv2.putText(img, 'ID:' + str(id), (int(point[0] + 5), int(point[1] - 100)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 255), 1)
        cv2.putText(img, 'TYPE:' + str(type), (int(point[0] + 5), int(point[1] - 85)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 255), 1)
        cv2.putText(img, 'WEIGHT:' + str(weight), (int(point[0] + 5), int(point[1] - 70)), cv2.FONT_HERSHEY_COMPLEX,
                    0.5, (0, 0, 255), 1)
    if flag == 3:
        cv2.rectangle(img, p1, p2, color, thick)
        cv2.line(img, (int(point[0]), int(point[1])), (int(point[0]), int(point[1] + 110)), (0, 0, 255), 1)
        cv2.putText(img, 'ID:' + str(id), (int(point[0] + 5), int(point[1] + 80)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 255), 1)
        cv2.putText(img, 'TYPE:' + str(type), (int(point[0] + 5), int(point[1] + 95)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 255), 1)
        cv2.putText(img, 'WEIGHT:' + str(weight), (int(point[0] + 5), int(point[1] + 110)), cv2.FONT_HERSHEY_COMPLEX,
                    0.5, (0, 0, 255), 1)
    if flag == 4:
        cv2.rectangle(img, p1, p2, color, thick)
        cv2.line(img, (int(point[0]), int(point[1])), (int(point[0]), int(point[1] + 140)), (0, 0, 255), 1)
        cv2.putText(img, 'ID:' + str(id), (int(point[0] + 5), int(point[1] + 110)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 255), 1)
        cv2.putText(img, 'TYPE:' + str(type), (int(point[0] + 5), int(point[1] + 125)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 255), 1)
        cv2.putText(img, 'WEIGHT:' + str(weight), (int(point[0] + 5), int(point[1] + 140)), cv2.FONT_HERSHEY_COMPLEX,
                    0.5, (0, 0, 255), 1)

    return img

class object():
    flag = 0
    point = ()
    id = ''
    tpye = ''
    weight = ''

cap = cv2.VideoCapture('C:\\Users\yunxu\\Desktop\\jtl\\1_2.avi')

tf, img = cap.read()

nFps = cap.get(cv2.CAP_PROP_FPS)
print(nFps)
delay = int(1000/nFps)
print(delay)
time = 0
'''
车道位置：
1  548 183    距离: 548 - 207 = 341  373 440 
2  548 217
3  207 254
4  207 289
'''

# 1：4车道位置中央 0s  7s truck  0-175
object1 = object()    # 548 - 375 = 173
object1.flag = 4
object1.point = (375, 289)   # 175  173/175 = 1
object1.id = '1'
object1.type = 'truck'
object1.weight = '15000kg'

# 2: 2车道起始    11s  25s car  14 * 25 = 350   275-625
object2 = object()   # 341 / 350 = 0.97
object2.flag = 2
object2.point = (548, 217)
object2.id = '2'
object2.type = 'car'
object2.weight = '2001kg'

# 3: 4车道起始    17s  28s truck 11 * 25 = 275   425-700
object3 = object()   # 341 / 275 = 1.24
object3.flag = 4
object3.point = (207, 289)
object3.id = '3'
object3.type = 'truck'
object3.weight = '11000kg'

# 4: 3车道起始     19s  29s car 10 * 25 = 250   475-725
object4 = object()   # 341/250 = 1.364
object4.flag = 3
object4.point = (207, 254)
object4.id = '4'
object4.type = 'car'
object4.weight = '2001kg'

# 5: 4车道起始    31s   40s car 9 * 25 = 225    775-1000
object5 = object()  # 341/225 = 1.51
object5.flag = 4
object5.point = (207, 289)
object5.id = '5'
object5.type = 'car'
object5.weight = '2001kg'

# 6: 3车道起始   34s   43s  car 9 * 25 =225   850-1075
object6 = object()  # 341 / 225 = 1.51
object6.flag = 3
object6.point = (207, 254)
object6.id = '6'
object6.type = 'car'
object6.weight = '2001kg'

# 7: 2车道起始   33s   45s  car 12 * 25 = 300  825-1125
object7 = object() # 341/300 = 1.14
object7.flag = 2
object7.point = (548, 217)
object7.id = '7'
object7.type = 'car'
object7.weight = '2001kg'

list_t1 = list(object1.point)
list_t2 = list(object2.point)
list_t3 = list(object3.point)
list_t4 = list(object4.point)
list_t5 = list(object5.point)
list_t6 = list(object6.point)
list_t7 = list(object7.point)

while(tf):



    if time < 175:
        img = drawing(object1.flag, list_t1, object1.id, object1.type, object1.weight,img)
        list_t1[0] = list_t1[0] + 1
    if time > 275 and time < 625:
        img = drawing(object2.flag, list_t2, object2.id, object2.type, object2.weight, img)
        list_t2[0] = list_t2[0] - 0.97
    if time > 425 and time < 700:
        img = drawing(object3.flag, list_t3, object3.id, object3.type, object3.weight, img)
        list_t3[0] = list_t3[0] + 1.24
    if time > 475 and time < 725:
        img = drawing(object4.flag, list_t4, object4.id, object4.type, object4.weight, img)
        list_t4[0] = list_t4[0] + 1.364
    if time > 755 and time < 1000:
        img = drawing(object5.flag, list_t5, object5.id, object5.type, object5.weight, img)
        list_t5[0] = list_t5[0] + 1.51
    if time > 850 and time < 1075:
        img = drawing(object6.flag, list_t6, object6.id, object6.type, object6.weight, img)
        list_t6[0] = list_t6[0] + 1.51
    if time > 825 and time < 1125:
        img = drawing(object7.flag, list_t7, object7.id, object7.type, object7.weight, img)
        list_t7[0] = list_t7[0] - 1.14



    time += 1
    print(time)
    cv2.imshow('img',img)
    cv2.waitKey(delay - 8)
    tf, img = cap.read()





