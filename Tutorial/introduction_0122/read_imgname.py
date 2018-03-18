import os
from numpy import *
from PIL import Image


def img2array(path, files):

    value = zeros([1, 28, 28, 1])
    value[0, 0, 0, 0] = -1
    labels = zeros([1, 10])
    labels[0, 0] = -1


    for file in files:
        if os.path.splitext(file)[1] == '.png':
            file = path + '/' + file
            img = array(Image.open(file).convert('L'))
            #print(img)
            width, height = shape(img)
            tmp_value = zeros([1, width, height, 1])
            for i in range(width):
                for j in range(height):
                    tmp_value[0, i, j, 0] = img[i, j]
            #print(tmp_value)
            if value[0, 0, 0, 0] == -1:
                value = tmp_value
            else:
                value = concatenate((value, tmp_value))
            index = int(file.strip().split('/')[1][0])
            label = zeros([1, 10])
            label[0, index] = 1

            if labels[0, 0] == -1:  #将所有label连起来 合为labels 第一次判断为True 之后都为 False
                labels = label
            else:
                labels = concatenate((labels, label))
    return array(value), array(labels)

# path = 'test_num'
# files = os.listdir(path)
# img2array(path, files)


