# Select randomly a 'good' frame for each video

import os
import shutil
import random

# PATH = 'E:/EmotiW2017/Train_AFEW'
PATH = 'E:/EmotiW2017/Val_AFEW'
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
        os.makedirs(PATH + '/face_images/' + d)

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
                    shutil.copy(jpg_full_name, PATH + '/face_images' + '/' + d + '/' + jpg_file)

                    num_of_files += 1

print(str(num_of_files) + ' files found.')