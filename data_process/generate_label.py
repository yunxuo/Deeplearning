import cv2
import tkinter
import random
from create_xml import create_xml, get_image_size
# from pre_work.select_key_image import numFiles
# from input_label import *
import os
import numpy as np
import time


path_image = 'E:\deeplearning\Image\pascal\JPEGImages\JPEGImages'
path_save = 'xml/'

def numFiles(path):
    i = 0
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.jpg':
            i += 1
    return i



# 创建窗体输入函数
def get_text():
    def go():
        global text_class
        text_class.append(entry.get())
        win.destroy()

    win = tkinter.Tk(className='input label')
    win.geometry('230x100')  # 这里用x 而不是*

    label = tkinter.Label(win)
    label['text'] = 'input label: '
    label.pack()  # 加载到窗体

    entry = tkinter.Entry(win)
    entry.pack()

    tkinter.Button(win, text='ok', command=go).pack()
    # a = go()

    win.mainloop()
# 创建回调函数
add_flag = False
copy_flag = False
text_class = []
positions = []
def on_mouse(event, x, y, flags, param):
    global add_flag, text_class, copy_flag, positions, ix1, iy1, ix2, iy2
    color = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 127, 255 ), (0, 0, 255), (139, 0, 255), (0, 0, 0)]

    # 当按下左键是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        copy_flag = False
        add_flag = True
        ix1, iy1 = x, y
    # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        copy_flag = False
        add_flag = True
        ix2, iy2 = x, y
        cv2.rectangle(param, (ix1, iy1), (ix2, iy2), (255, 255, 255), -1)

    # 当鼠标松开停止绘画。
    elif event == cv2.EVENT_LBUTTONUP:
        copy_flag = True
        add_flag = False
        cv2.rectangle(param, (ix1, iy1), (ix2, iy2), random.choice(color), 1)
        get_text()
        positions.append(int(ix1))
        positions.append(int(iy1))
        positions.append(int(ix2))
        positions.append(int(iy2))
        print(positions)
        print(text_class)





item = 0
former_flag = 0
total_image = numFiles(path_image)
all_image = os.listdir(path_image)

while item != total_image:

    image = all_image[item]

    if former_flag == 1:  # 防止索引值小于0
        if item <= 0:
            item = 0
        else:
            item -= 1
        image = all_image[item]

    if os.path.isfile(os.path.join(path_image, image)):
        if os.path.splitext(os.path.join(path_image, image))[1] == '.jpg':
            former_flag = 0
            print('Now process: %s\tProcessing:%0.2f'%(image, item*100/total_image) + '%')

            img = cv2.imread(os.path.join(path_image, image))
            temp = img.copy()

            put_text = 'image: %s' % (image)
            # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
            cv2.putText(img, put_text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            xml_name = os.path.splitext(image)[0] + '.xml'
            xml_file = os.path.join(path_save, xml_name)
            nWidth, nHeigth = get_image_size(os.path.join(path_image, image))

            cv2.namedWindow('image')
            cv2.setMouseCallback('image', on_mouse, img)

            while True:
                if add_flag:
                    cv2.addWeighted(temp, 0.7, img, 0.3, 0, img)
                if copy_flag:
                    temp = img.copy()
                cv2.putText(img, put_text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow('image', img)
                key = cv2.waitKey(50) & 0xFF
                if key == ord('q') or key == 27:
                    break
                elif key == ord('6'):   # next image
                    item += 1
                    if len(text_class) > 0:
                        create_xml(image, nWidth, nHeigth, text_class, positions, xml_file)
                        print('%s file saved to ---> %s file'%(image, xml_name))
                        add_flag = False
                        copy_flag = False
                        text_class = []
                        positions = []
                    break
                elif key == ord('4'):   # former image
                    former_flag = 1
                    break
            #     else:
            #         break
            if key == ord('q') or (key & 0xff) == 27:
                break