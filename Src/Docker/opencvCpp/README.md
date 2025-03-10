
- build
```
# 参考: https://www.kkaneko.jp/tools/ubuntu/ubuntu_opencv.html

git clone https://github.com/Itseez/opencv.git
git clone https://github.com/Itseez/opencv_contrib.git

cmake   -D CMAKE_INSTALL_PREFIX=/usr/local \
  -DBUILD_opencv_world=ON \
  -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
  -DINSTALL_TESTS=ON \
  -DINSTALL_C_EXAMPLES=ON \
  -DWITH_PYTHON=ON \
  -DINSTALL_PYTHON_EXAMPLES=ON \
  -DBUILD_opencv_python2=OFF \
  -DBUILD_opencv_python3=ON \
  -DPYTHON_DEFAULT_EXECUTABLE=python3 \
  -DBUILD_EXAMPLES=ON .. \
  ../opencv


# mainのビルド
cd build
sudo cmake ..
sudo make
```


# build
```
cd Src/libs
git clone https://github.com/eigenteam/eigen-git-mirror

mkdri build
cd build
sudo cmake ..
sudo make
```

