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
4. CUDA 8.0
5. cuDNN v5
6. OpenCV
7. Libraries: natsort, pydot, sklearn, libplotmat (using `pip install ...`), and [graphviz](http://www.graphviz.org/Download_windows.php)
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
### Install OpenCV with Anaconda support
1. Enter `conda install -c https://conda.binstar.org/menpo opencv3`
2. Validate installation by entering `python -c "import cv2; print(cv2.__version__)"`
## Usage
### Face extraction (2 options)
1. (**Recommended**) Download and extract **already extracted** face images from `\\168.131.152.92\emotion\Duong\AFEW_7_2017\face_images` to a folder (D:\AFEW2017 for example)
---
- `afew2017_aligned_extracted_faces_cascade_cnn.rar` contains `ALIGNED` face images:  
![alt text](https://raw.githubusercontent.com/nhduong/afew2016/master/imgs/aligned.jpg)
- `afew2017_aligned_extracted_faces_cascade_cnn.rar` contains `UNALIGNED` face images:  
![alt text](https://raw.githubusercontent.com/nhduong/afew2016/master/imgs/unaligned.jpg)
---
2. (*Skip this step in case you've already downloaded images from option 1*) Manually extract face images:
- Download and extract original AFEW2017 dataset from `\\168.131.152.92\emotion\Duong\AFEW_7_2017\2017_EmotiW.zip` to a folder, such as D:\AFEW2017
- Download video converter from `\\168.131.152.92\emotion\Duong\AFEW_7_2017\avi_to_mp4.py` and save it in `D:\AFEW2017\Train_AFEW` and `D:\AFEW2017\Val_AFEW`
- Open cmd:
  - Type `cd /d D:\AFEW2017\Train_AFEW`, and enter `python avi_to_mp4.py`
  - Type `cd /d D:\AFEW2017\Val_AFEW`, and enter `python avi_to_mp4.py`
- Install mxnet
  - Download `prebuildbase_win10_x64_vc14.7z` and `20170718_mxnet_x64_vc14_gpu.7z` from `\\168.131.152.92\emotion\Duong\AFEW_7_2017\mxnet`
  - Extract `prebuildbase_win10_x64_vc14.7z` to a folder, such as D:\mxnet
  - Extract and overwrite `20170718_mxnet_x64_vc14_gpu.7z` to the above folder
  - Run `setupenv.cmd` as Administrator
  - Open `cmd` as Administrator
  - Type `cd /d D:\mxnet\python`
  - Enter `python setup.py install`
  - Press `python -c "import mxnet; print(mxnet.__version__)"` to validate installation
- Download `mtcnn_detector.py`, and `afew2017_face_extraction_from_mp4s.ipynb` from this repo and save them in a folder (called `E2017`)
- Download Cascade CNN model from `\\168.131.152.92\emotion\Duong\AFEW_7_2017\mxnet\cascade_cnn.rar` and extract all the contents into `E2017\model`
- Open cmd, type `cd /d E2017`
- Enter `jupyter notebook` to run Jupyter IDE
- Open `afew2017_face_extraction_from_mp4s.ipynb`
- Modify `PATH = 'E:/EmotiW2017/Val_AFEW/' + video_path`, and `PATH2 = 'E:/EmotiW2017/lstm/Val_AFEW/' + video_path` based on the extracted AFEW2017 dataset path on your computer
- `Run All Cell` (Cell > Run All Cell)
- Change `Val_AFEW` to `Train_AFEW` in `PATH` and `PATH2`. Run all cell again to extract faces from the training set  
  
Note that: the extracted images will be saved in `PATH2`
### Run CNN-LSTM source code
1. Download `afew2017_cnn_lstm_with_data_processing.ipynb` from this repo and save it to a folder (called `E2017`)
2. Open cmd, type `cd /d E2017`
3. Enter `jupyter notebook` to run Jupyter IDE
4. Open `afew2017_cnn_lstm_with_data_processing.ipynb`
5. The training results are already done in `In [56]`-`In [59]`
6. In order to retrain:
- modify `PATH = 'E:/EmotiW2017/lstm/original/Train_AFEW'`, and `PATH = 'E:/EmotiW2017/lstm/original/Val_AFEW'` based on the extracted face images path on your computer
- `Run All Cell` (Cell > Run All Cell)
  
  
Backup M:\CNU\EmotiW\2016\Face_detection\caffe_python_mtcnn-master