# EmotiW 2016: Facial Expression Recognition in the Wild
Nguyen Hai Duong (nhduong_3010@live.com)  
Chonnam National University  
  
  
Note that:
- In Windows 7, type `cd /d path` to change working directory
- In Windows 10, type `cd path` instead

## Requirements
1. Windows 7/10 Pro x64
2. Anaconda 4.2 Python 3.5
3. TensorFlow 1.1.0 with Keras interface
4. Visual Studio 2015 (MSCV 14) for compiling Caffe
5. CUDA 8.0
6. cuDNN v5
7. Caffe for Windows
8. OpenCV
9. Libraries: numpy, imageio, and libplotmat
## Installation
### Install CUDA 8.0, cuDNN v5, NVIDIA driver, and Visual Studio 2015
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
### Build Caffe on Windows
1. Download and install [CMake 3.9](https://cmake.org/files/v3.9/cmake-3.9.0-rc5-win64-x64.msi)
2. Close all cmd windows
3. Open cmd as administrator again
4. Enter `conda config --add channels conda-forge`, `conda config --add channels willyd`, and `conda install --yes cmake ninja numpy scipy protobuf==3.1.0 six scikit-image pyyaml pydotplus graphviz`
5. Enter `cd /d <where/to/download/caffe>`
6. Enter `git clone https://github.com/BVLC/caffe.git` to download Caffe
7. Enter `cd /d caffe`
8. Enter `git checkout windows`
9. Open `scripts\build_win.cmd` with Notepad, find and replace
```
if NOT DEFINED WITH_NINJA set WITH_NINJA=1 ---> if NOT DEFINED WITH_NINJA set WITH_NINJA=0
if NOT DEFINED CPU_ONLY set CPU_ONLY=1 ---> if NOT DEFINED CPU_ONLY set CPU_ONLY=0
set CONDA_ROOT=C:\Miniconda35-x64 ---> set CONDA_ROOT=C:\Program Files\Anaconda3
```
10. Type `scripts\build_win.cmd`, and press Enter
11. Copy all files and folders in `<where/to/download/caffe>\python\caffe` to `C:\Program Files\Anaconda3\Lib\site-packages\caffe`
12. Validate Caffe installation by entering `python -c "import caffe; print(caffe.__version__)"`
### Install some libraries
1. Open cmd as administrator again
2. Enter `pip install imageio`, and `conda install ffmpeg -c conda-forg`
## Usage
1. Download all files from this repo and store them in a specific path (called `EMO`)
2. Download trained model `fer2013_weights.h5` from `\\168.131.152.92\emotion\Duong` and save it to `EMO`
3. Create `model` folder in `EMO`, download `\\168.131.152.92\emotion\Duong\model.rar` and extract all files in this archive to `EMO\model`
4. Download testing video `\\168.131.152.92\emotion\Duong\004004880.avi.mp4` and save it to `EMO`
5. Open cmd, type `cd /d EMO`
6. Enter `jupyter notebook` to run Jupyter IDE
7. Open `demo.ipynb`, and `Run All Cell` (Cell > Run All Cell)

* Backup M:\CNU\EmotiW\2016\Face_detection\caffe_python_mtcnn-master