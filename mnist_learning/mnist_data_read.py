from PIL import Image
import struct
import cv2
import os

# '>'     Big-Endian format
# 'II'    two integer
# 'IIII'  four integer
# '784B'  the size of image is 28 * 28,which need 784 byte
# '1B'    label is 1 byte

#use function as u

def read_images(filename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()
    f.close()

    magic, images, rows, columns = struct.unpack_from('>IIII', buf, index)
    index += struct.calcsize('IIII')

    for i in range(images):
        image = Image.new('L', (columns, rows))

        for x in range(rows):
            for y in range(columns):
                image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
                index += struct.calcsize('>B')

        print('save' + str(i) + 'image')
        image.save('test_img\\' + str(i) + '.png')


def read_labels(filename):
    f = open(filename, 'rb')
    buf = f.read()
    index = 0
    f.close()
    magic, num_items = struct.unpack_from('>II', buf, index)
    index += struct.calcsize('II')
    labels = []
    for i in range(num_items):
        value = struct.unpack_from('>B', buf, index)
        index += struct.calcsize('B')
        labels.append(value[0])
    print(labels)

    fp = open('labels.txt', 'w')
    text = ''
    for i in range(6000):
        text = text + 'The %d picture is: '%(i) + str(labels[i]) +'\n'
    fp.write(text)
    fp.close()

