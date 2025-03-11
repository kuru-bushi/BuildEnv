
# build
```
# ファイルの配置
--------------------
(任意のディレクトリ)
├ pybind11(リポジトリ)
├ CMakeLists.txt
├ mycat.cpp
└ build
--------------------

# pybind11 クローン
git clone {pybind}

# build
mkdir build
cd build
cmake ..
make

# 確認方法
下記のような .so ファイルができているはず。python や arch のバージョンによって生成ファイル名が異なる。
./build/mycat.cpython-38-aarch64-linux-gnu.so

```