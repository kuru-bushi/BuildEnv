pybind11 のチュートリアル用テンプレート

# build
```
# ファイルの配置
--------------------
(任意のディレクトリ)
├ pybind11(リポジトリ)
├ CMakeLists.txt
├ mycat.cpp
├ main.py
└ build
--------------------

# pybind11 クローン
git clone {pybind}
commit: 06e8ee2e357fc2fd6e36de431fa0ca0049aafc7d

# build
mkdir build
cd build
cmake ..
make
```

下記のような .so ファイルができているはず。python や arch のバージョンによって生成ファイル名が異なる。
./build/mycat.cpython-38-aarch64-linux-gnu.so

.so ファイルを imoprt して C+ を呼び出す

## 動作確認方法
```
$ python main.py
Shiro said meow.
```
