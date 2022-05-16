import cv2
import os
import time
import uuid

IMAGES_PATH = r'C:\Users\bipla\FYP\Sign-Language-Detection-B7\Tensorflow\workspace\images\collectedimages-biplab'

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    path = r'C:\Users\bipla\FYP\Sign-Language-Detection-B7\Tensorflow\workspace\images\collectedimages-biplab\\' + label
    os.mkdir(path)
    cap = cv2.VideoCapture(0)
    print('Collecting Images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
