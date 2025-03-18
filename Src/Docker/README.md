# 概要
- 各ディレクトリについて
```
libs: C++ のライブラリのビルド用ディレクトリ。libs/{library}/build ディレクトリでビルド
data: Python, C++ のデータ保存用ディレクトリ
その他: ディレクトリ名のナレッジのスクリプトを保存
```



# build
## python docker(python3_10_0/Dockerfile)
```
docker build -t {イメージ名} {Dockerfile のパスがあるディレクトリ}

docker run -it -d -v $(pwd):/home --name python_test_cnt python_test /bin/bash
```

## Extended-Kalman-Filter
- カルマンフィルタのチュートリアル
- shell を実行することで解析結果が画像で保存される
```
https://github.com/uNetworking/uWebSockets.git
git clone https://github.com/uWebSockets/uWebSockets

# ビルド
https://github.com/zhujun98/behavior-and-path-planning/issues/1
```

# kalman_filter
```
# docker containerのビルド ubuntu:20.04
docker build -t {イメージ名} {Dockerfile のパスがあるディレクトリ}
docker run -t -i -d  -v $(pwd):/home --name cpp_tutorial_cnt cpp_tutorial /bin/bash

# github 
git clone https://github.com/remmaTech12/kalman_filter.git


# パッケージ管理ツール
apt-get update
apt-get install cmake make -y
apt-get install gcc -y
apt-get install libeigen3-dev -y
apt-get install libgtest-dev -y
apt install gnuplot

# 修正
Eigen/Dence -> eigen3/Eigen/Dence
```

## yolo object detection
```

git clone https://github.com/ultralytics/ultralytics.git
ln -s /usr/bin/python3 /usr/bin/python
apt-get install python3-pip

python -m pip install -U pip

# 必要なライブラリのダウンロード
python -m pip install ultralytics

# 学習のナレッジ
https://docs.ultralytics.com/ja/datasets/detect/coco/#dataset-yaml

# データセットのダウンロード
wget http://images.cocodataset.org/zips/val2017.zip
参考: https://gist.github.com/mkocabas/a6177fc00315403d31572e17700d7fd9

```


## pybind
- python から C+ の呼び出し。.so ファイルをインポート
```
pybind/README参照
```






