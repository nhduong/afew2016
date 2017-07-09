import os
import shutil

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
                # Find jpgs
                for jpg_file in os.listdir(PATH + '/' + d + '/' + dd):
                    if jpg_file.endswith('.jpg'):
                        # Combine path and file name
                        jpg_full_name = PATH + '/' + d + '/' + dd + '/' + jpg_file

                        shutil.copy(jpg_full_name, PATH + '/face_images' + '/' + d + '/' + jpg_file)

                        num_of_files += 1

print(str(num_of_files) + ' files found.')