# -*- coding: cp936 -*-

from tkinter import *

text_class = ''

def get_text():
    def go():
        global text_class
        text_class = entry.get()
        win.destroy()

    win = Tk(className='input label')
    win.geometry('230x100')  # 这里用x 而不是*

    label = Label(win)
    label['text'] = 'input label: '
    label.pack()  # 加载到窗体

    entry = Entry(win)
    entry.pack()

    Button(win, text='ok', command=go).pack()
    # a = go()

    win.mainloop()


