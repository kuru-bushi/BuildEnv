docker build -t python_test


# docker run -t -d -v (ホストサーバマウント先):(コンテナマウント先) --name コンテナ名 イメージ名 {コマンド}
docker run -it -d -v $(pwd):/home --name python_test_cnt python_test /bin/bash



# build
```
apt -y update
apt -y install libopencv-dev

# libs ディレクトリ
git clone {opencv のURL}
mkdir build
cd build
cmake ..


# プロジェクトディレクトリ
mkdir build
cd build
cmake ..

```

## モデルのダウンロード

```
# yolo
https://docs.ultralytics.com/ja/models/yolo-world/#available-models-supported-tasks-and-operating-modes
```
### その他サイト
- NVIDIA TAO Toolkit
- hugging face
- Qualcomm AI Hub
- Civitai


