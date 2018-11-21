import cv2
import os
import shutil

'''实现功能
按键1：挑选图片
按键2：撤销上一张保存的操作
按键4：上一张
按键5：下一张
按键q或者Esc：退出


'''

path_image = 'E:/track/image'
path_selected = os.path.join(path_image,'selected/')
path_no_want = ''


if not os.path.isdir(path_selected):
    os.mkdir(path_selected)



# Rename file in path ,start at num
def RenameFile(path, num):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if os.path.splitext(os.path.join(path, file))[1] == '.jpg':
                newname = '%06d' % (num) + '.jpg'
                os.rename(os.path.join(path, file), os.path.join(path, newname))
                num += 1
                print(file, '--->', newname)

# return the total num of image
def numFiles(path):
    i = 0
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.jpg':
            i += 1
    return i


# copy the file from input_path to output_path
def CopyFile(input_path,output_path,file):
    shutil.copyfile(os.path.join(input_path,file),os.path.join(output_path,file))



item = 0
former_flag = 0  # return to the former image
delete_flag = 0  # delete the just saved image
total_image = numFiles(path_image)
all_image = os.listdir(path_image)

while item != total_image:
    image = all_image[item]

    if former_flag == 1:
        if item <= 0:
            item = 0
        else:
            item -= 1
        image = all_image[item]

    if delete_flag == 1:
        if os.path.exists(os.path.join(path_selected, image)):
            os.remove(os.path.join(path_selected, image))

    if os.path.isfile(os.path.join(path_image, image)):
        if os.path.splitext(os.path.join(path_image, image))[1] == '.jpg':
            former_flag = 0
            delete_flag = 0
            print('Now process: %s \t Processing:%0.2f'%(image, item*100/total_image) + '%')
            img = cv2.imread(os.path.join(path_image, image))
            text = 'image: %s'%(image)
            cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)   # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
            cv2.imshow('Process', img)
            key = cv2.waitKey(0)
            while True:
                if key == ord('q') or (key & 0xff) == 27:
                    break
                elif key == ord('1'):
                    CopyFile(path_image,path_selected,image)
                    print('%s save to: %s'%(image, path_selected))
                    item += 1
                    break
                elif key == ord('2'):
                    former_flag = 1
                    delete_flag = 1
                    break
                elif key == ord('6'):   # next image
                    item += 1
                    break
                elif key == ord('4'):   # former image
                    former_flag = 1
                    break
                else:
                    break
            if key == ord('q') or (key & 0xff) == 27:
                break

cv2.destroyAllWindows()
