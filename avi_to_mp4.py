import os
import subprocess

print('> converting avi ---> mp4...')

num_of_files = 0

# List of dirs (Angry, Disgust, etc.)
for d in os.listdir('./'):
    if os.path.isdir(d):
        # Find .avi in each folder
        for avi_file in os.listdir('./' + d):
            if avi_file.endswith('.avi'):
                # Combine path and file name
                avi_full_name = './' + d + '/' + avi_file
                # print('before')
                # subprocess.call(['ffmpeg', '-i', avi_full_name, '-c:v', 'libx264', '-crf', '19', '-preset', 'slow', '-c:a', 'aac', '-b:a', '192k', '-ac', '2', '-loglevel', 'panic', '-y', avi_full_name + '.mp4'])
                subprocess.call('ffmpeg -i ' + avi_full_name + ' -c:v libx264 -crf 19 -preset slow -c:a aac -b:a 192k -ac 2 -loglevel panic -y ' + avi_full_name + '.mp4', shell=True)

                num_of_files += 1

print(num_of_files + ' files found.')