# Nerf-Sentry-Gun
An object tracking Nerf Sentry Gun
Forked from BuckarewBanzai

Uses OpenCv, Numpy, and Yolov3

Download Yolov3 weights since the file is way too big to put in the repo (Make sure to download [YOLOv3-320](https://pjreddie.com/darknet/yolo/) weights since it was built on this!)



I will try to see if this works on a raspberry pi 4, so that you can build a Nerf sentry gun

below this text is all you need to do for gun.py to work
```bash  
pip install git+https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library 
```

Make sure to create your virtual environment with the extra flag.

```bash
mkvirtualenv cv --system-site-packages -p python2
```

Source your bash profile

```bash
source ~/.profile
```

Activate your virtual environment

```
workon cv
```

Clone this repository

```
git clone git@github.com:waterbottle-123/Nerf-Sentry-Gun
```

Navigate to the directory

```
cd Nerf-Sentry-Gun
```

Install dependencies to your virtual environment

```
pip install imutils RPi.GPIO
```

Run the project!

```
python gun.py
```

## Setting Parameters

gun.py has a couple parameters that you can set.

```python
### User Parameters ###

MOTOR_X_REVERSED = False
MOTOR_Y_REVERSED = False

MAX_STEPS_X = 30
MAX_STEPS_Y = 15

RELAY_PIN = 22

#######################
```

These will be located at the top of the file. Use `vim gun.py` to open the file. Press `i` to edit.
Once you've made your changes, press `esc` then `ZZ` to save.
