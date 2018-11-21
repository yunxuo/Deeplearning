import os
import random
"""
 train : val : test = 6 : 2 : 2
"""

xml_path = 'E:/deeplearning/Image/2018-01-17/ImageXml'
save_path = 'E:/deeplearning/Image/2018-01-17/'

trainval_percent = 0.8
train_percent = 0.7
all_xml = os.listdir(xml_path)
num = len(all_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)


trainval = random.sample(list, tv)  # sample tv samples to trainval from list
train = random.sample(trainval, tr)


print('train size: ', tr)
print('val size: ', tv - tr)
print('test size: ', num - tv)

ftrainval = open(os.path.join(save_path, 'VOC2007/ImageSets/Main/trainval.txt'), 'w')
ftest = open(os.path.join(save_path, 'VOC2007/ImageSets/Main/test.txt'), 'w')
ftrain = open(os.path.join(save_path, 'VOC2007/ImageSets/Main/train.txt'), 'w')
fval = open(os.path.join(save_path, 'VOC2007/ImageSets/Main/val.txt'), 'w')


for i in list:
    name = os.path.splitext(all_xml[i])[0] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()