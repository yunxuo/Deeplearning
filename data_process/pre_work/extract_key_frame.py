import cv2
import os

video_path = 'E:/video'  # input the dir of video
video_name = 'Standard_SCU7TL_2017-12-08_1715.001.mp4'  # input the name of video

video_save_path = video_path + '/' + 'image/'

if not os.path.exists(video_save_path):
    os.makedirs(video_save_path)


video_file = os.path.join(video_path, video_name)
video = cv2.VideoCapture(video_file)

nFrame = video.get(cv2.CAP_PROP_FRAME_COUNT)
nFps = video.get(cv2.CAP_PROP_FPS)
format = video.get(cv2.CAP_PROP_MODE)
delay = int(1000/nFps)

print('Fps: %d\nFrame: %d'%(nFps, nFrame))
print(format)

nCount = 0

while nCount != nFrame:
    ret, frame = video.read()
    imagename = os.path.join(video_save_path, '%06d.jpg' % (nCount))
    # imagename = '%06d.jpg' % (nCount)
    if nCount % int(5 * nFps) == 0:
        cv2.imwrite(imagename, frame)
        cv2.imshow('extract', frame)
        cv2.waitKey(500)
        cv2.destroyWindow('extract')
        print(nCount)
    # cv2.imshow('frame', frame)
    # key = cv2.waitKey(2) & 0xff
    # if key == ord('q'):
    #     break
    nCount += 1


video.release()
cv2.destroyAllWindows()
