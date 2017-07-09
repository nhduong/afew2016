# Convert external images from Kaggle fer2013 to rgb and copy them to the face_images folder

import os
import shutil
import sys
import cv2

PATH = 'E:/EmotiW2017/Train_AFEW'
FER2013 = 'D:/Github/afew2016/data/fer2013/train'

num_of_files = 0

# Where to save jpgs
if not os.path.isdir(PATH + '/face_images'):
    print('./face_images does not exist')
    sys.exit(0)

# List of dirs (Angry, Disgust, etc.)
for d in os.listdir(FER2013 + '/'):
    if os.path.isdir(FER2013 + '/' + d):
        print(FER2013 + '/' + d)
        for jpg_file in os.listdir(FER2013 + '/' + d):
            if jpg_file.endswith('.jpg'):
                jpg_full_name = FER2013 + '/' + d + '/' + jpg_file
                img = cv2.imread(jpg_full_name)

                img = cv2.resize(img, (224, 224))
                if len(img.shape) <= 2:
                    img = backtorgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                cv2.imwrite(PATH + '/face_images' + '/' + d + '/' + jpg_file, img)
                # shutil.copy(jpg_full_name, PATH + '/face_images' + '/' + d + '/' + jpg_file)
                
                num_of_files += 1

print(str(num_of_files) + ' files found.')