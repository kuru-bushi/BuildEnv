

# build
### ultralytics(yolo)
- ONNX
```
# clone
git clone https://github.com/ultralytics/ultralytics.git

# train
## install
python -m pip install ultralytics

## deepsparseを入れた後、エラーを吐いたので、再度インストールしたら動作した。
## coco8.yaml, yolo11n.pt は ultralytics からダウンロード
## coco8のダウンロード(不要だと思われる)
## download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8.zip
## pt モデルはルートに保存されていた /ultralytics/runs/detect/train7/weights/, yolo のコマンドを打った時、「 save_dir=/ultralytics/runs/detect/train7」というパスが表示されるためログを確認

yolo detect train data=coco8.yaml model=yolo11n.pt epochs=100 imgsz=640
## 参考: https://docs.ultralytics.com/ja/modes/train/#usage-examples
## format=onnx にすればフォーマットの指定も可能
# yolov11 は DeepSparseがサポートしていない yolo detect train data=coco8.yaml model=yolo11n. epochs=100 imgsz=640

## onnx に変換
mv /ultralytics/runs/detect/train7/weights/last.pt ./yolo8n.pt
yolo task=detect mode=export model=yolov8.pt format=onnx opset=13


# predict
DeepSparse は yolov11 に公式に対応できていないという旨のイシューを見つけた(2025/3/12)
https://github.com/ultralytics/ultralytics/issues/17528

## (暫定策)今の DeepSparse だとエラーが出る。古いバージョンに戻す?
## DeepSparse は Intelでしか動かない。 M1では動作しない。
python -m pip install -U ultralytics==8.0.124
python3 prediction_onnx.py


# transformation ONNX
## pytorch の load_dict でロードして onnx に変換する必要がある。yolo は CLI で全て完結できる。
## yolo11n.onnx が出力される
yolo export model=yolo11n.pt format=onnx
```

- 量子化(Deepsparse)
```
# Deepsparse で量子化(Intel で動作(未検証))
# https://docs.ultralytics.com/ja/integrations/neural-magic/#step-2-exporting-yolo11-to-onnx-format
python -m pip install deepsparse[yolov8]

# ベンチマーク
deepsparse.benchmark model_path="/home/python_yolov/yolo11n.onnx" --scenario=sync --input_shapes="[1,3,640,640]"
```
- 量子化
```
$ python -m pip install onnx onnxruntime onnxconverter-common
$ python quantization_onnx.py
```

# 可視化
- QOperator
(更新予定)



# dataset
```
coco8 ダウンロード
https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8.zip
```


# 参考
```
# huggingface のモデルを ONNX に変換
https://docs.neuralmagic.com/guides/onnx/
```