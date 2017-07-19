# EmotiW 2016: Facial Expression Recognition in the Wild
Nguyen Hai Duong (nhduong_3010@live.com)  
Chonnam National University  
  
  
## Note that
- In Windows 7, type `cd /d path` to change working directory
- In Windows 10, type `cd path` instead

## Requirements
1. Windows 7/10 Pro x64
2. Anaconda 4.2 Python 3.5
3. TensorFlow 1.1.0 with Keras interface
5. CUDA 8.0
6. cuDNN v5
8. OpenCV
9. Libraries: natsort, pydot, sklearn, libplotmat (using `pip install ...`), and [graphviz](http://www.graphviz.org/Download_windows.php)
## Installation
### Install CUDA 8.0, cuDNN v5, and NVIDIA driver
### Download and install [Anaconda 4.2 with Python 3.5](https://repo.continuum.io/archive/Anaconda3-4.2.0-Windows-x86_64.exe)
### Install TensorFlow 1.1.0
1. Close all cmd windows
2. Open cmd as administrator again
3. Enter `conda create -n tensorflow python=3.5`
4. Enter `activate tensorflow`
5. Enter `pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.1.0-cp35-cp35m-win_amd64.whl`
6. Validate installation by entering `python -c "import tensorflow as tf; print(tf.__version__)"`
### Install OpenCV with with Anaconda support
1. Enter `conda install -c https://conda.binstar.org/menpo opencv3`
2. Validate installation by entering `python -c "import cv2; print(cv2.__version__)"`
## Usage
### Face extraction (2 options)
1. Download extracted face images from \\168.131.152.92\emotion\Duong\AFEW_7_2017\face_images
---
- `afew2017_aligned_extracted_faces_cascade_cnn.rar` contains `ALIGNED` face images:  
![alt text](https://raw.githubusercontent.com/nhduong/afew2016/master/imgs/aligned.jpg)
- `afew2017_aligned_extracted_faces_cascade_cnn.rar` contains `UNALIGNED` face images:  
![alt text](https://raw.githubusercontent.com/nhduong/afew2016/master/imgs/unaligned.jpg)
---
1. Download all files from this repo and store them in a specific path (called `EMO`)
2. Download trained model `fer2013_weights.h5` from `\\168.131.152.92\emotion\Duong` and save it to `EMO`
3. Create `model` folder in `EMO`, download `\\168.131.152.92\emotion\Duong\model.rar` and extract all files in this archive to `EMO\model`
4. Download testing video `\\168.131.152.92\emotion\Duong\004004880.avi.mp4` and save it to `EMO`
5. Open cmd, type `cd /d EMO`
6. Enter `jupyter notebook` to run Jupyter IDE
7. Open `demo.ipynb`, and `Run All Cell` (Cell > Run All Cell)

* Backup M:\CNU\EmotiW\2016\Face_detection\caffe_python_mtcnn-master