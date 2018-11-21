import cv2
import tkinter
import random
# from input_label import *
import numpy as np
import time


img = cv2.imread('images/000050.jpg')
temp = img.copy()




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





cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)

while True:
    if add_flag:
        cv2.addWeighted(temp, 0.7, img, 0.3, 0, img)
    if copy_flag:
        temp = img.copy()
    cv2.imshow('image', img)
    k = cv2.waitKey(50) & 0xFF
    if k == ord('q') or k == 27:
        break