# Select randomly a 'good' frame for each video

import os
import shutil
import random
import cv2

def emo_to_int(emo):
    if emo == 'Angry':
        return '0'
    if emo == 'Disgust':
        return '1'
    if emo == 'Fear':
        return '2'
    if emo == 'Happy':
        return '3'
    if emo == 'Neutral':
        return '4'
    if emo == 'Sad':
        return '5'
    if emo == 'Surprise':
        return '6'

PATH = 'E:/EmotiW2017/Train_AFEW'
# PATH = 'E:/EmotiW2017/Val_AFEW'
print('> managing jpg files....')
num_of_files = 0

# Where to save jpgs
if os.path.isdir(PATH + '/face_images'):
    shutil.rmtree(PATH + '/face_images')
os.makedirs(PATH + '/face_images')

# List of dirs (Angry, Disgust, etc.)
for d in os.listdir(PATH + '/'):
    if os.path.isdir(PATH + '/' + d) and d != 'face_images':
        # Create class label folders
        print('  > processing ' + d + ' instances...')
        os.makedirs(PATH + '/face_images/' + emo_to_int(d))

        # Find folders containing extracted images from mp4s
        for dd in os.listdir(PATH + '/' + d):
            if os.path.isdir(PATH + '/' + d + '/' + dd):
                if os.listdir(PATH + '/' + d + '/' + dd):
                    # Find jpgs randomly
                    jpg_file = random.choice(os.listdir(PATH + '/' + d + '/' + dd))
                    
                    # Combine path and file name
                    jpg_full_name = PATH + '/' + d + '/' + dd + '/' + jpg_file

                    random_timeout = 0

                    while not jpg_file.endswith('.jpg') or os.stat(jpg_full_name).st_size < 2000:
                        jpg_file = random.choice(os.listdir(PATH + '/' + d + '/' + dd))
                        random_timeout += 1

                        # Skip video since the face is invalid
                        if random_timeout == 20:
                            break
                        
                        # Combine path and file name
                        jpg_full_name = PATH + '/' + d + '/' + dd + '/' + jpg_file

                    if random_timeout == 20:
                        random_timeout = 0
                        continue

                    if random_timeout > 0:
                        random_timeout = 0  

                    # Copy selected file
                    img = cv2.imread(jpg_full_name)

                    img = cv2.resize(img, (224, 224))
                    if len(img.shape) <= 2:
                        img = backtorgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                    cv2.imwrite(PATH + '/face_images' + '/' + emo_to_int(d) + '/' + jpg_file, img)
                    # shutil.copy(jpg_full_name, PATH + '/face_images' + '/' + emo_to_int(d) + '/' + jpg_file)

                    num_of_files += 1

print(str(num_of_files) + ' files found.')