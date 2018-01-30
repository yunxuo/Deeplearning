# Copyright 2016 Yun Xu.
# Adapted form the on the MNIST biginners tutorial by Google.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""
Pridict handwrite integer mnist databae

Script requires :
1) saved model
2)one png file
"""

import sys
import tensorflow as tf
import os
from PIL import Image, ImageFilter
from mnist_predict_func import *
import cv2

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


path = 'F:\yunxu\mnist\program\\test_img/5331.png'
im = Image.open(path).convert('L')

pixel_value = list(im.getdata())
print(pixel_value)
a = predictint(pixel_value)[0]
print(a)

text = 'The number is: ' + str(a)
print(text)
dispaly_image = cv2.resize(cv2.imread(path), (500, 500))
cv2.namedWindow('num', 0)
cv2.resizeWindow('num', 500, 500)
cv2.putText(dispaly_image, text, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

cv2.imshow('num', dispaly_image)
cv2.waitKey(0)
