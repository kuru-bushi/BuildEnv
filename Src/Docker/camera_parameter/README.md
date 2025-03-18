

## build/install
```
python3 -m venv env_camera_parameter
# 必要があれば ln -s /usr/local/bin/python3 /usr/local/bin/python

# activate
source env_camera_parameter/bin/activate

# deactivate
deactivate

# install
apt-get install libopencv-dev
python -m pip install numpy opencv-python matplotlib
python -m pip install ipykernel
```


