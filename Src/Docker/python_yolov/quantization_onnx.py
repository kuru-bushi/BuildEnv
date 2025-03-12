import onnx
from onnxruntime.quantization import quantize_dynamic, QuantType
from onnxconverter_common import float16
from onnxconverter_common import auto_mixed_precision

# Mixed Precision(the mixed precision tool must be run on a device with a GPU.)
### model = onnx.load("path/to/model.onnx")
### Assuming x is the input to the model
### feed_dict = {'input': x.numpy()}
### model_fp16 = auto_mixed_precision(model, feed_dict, rtol=0.01, atol=0.001, keep_io_types=True)
### onnx.save(model_fp16, "path/to/model_fp16.onnx")

# Float16 Conversion
# 動的量子化
model_origin = 'yolo11n.onnx'
model = onnx.load(model_origin)
model_fp16 = float16.convert_float_to_float16(model)
onnx.save(model_fp16, "yolo11n_fp16.onnx")


# Float32
model_quant = 'yolo11n_fp32.onnx'
quantized_model = quantize_dynamic(model_origin, model_quant)

