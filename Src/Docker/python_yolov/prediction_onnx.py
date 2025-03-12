from deepsparse import Pipeline

# Specify the path to your YOLO11 ONNX model
model_path = "yolo11n.onnx"

# Set up the DeepSparse Pipeline
yolo_pipeline = Pipeline.create(task="yolov8", model_path=model_path)

# Run the model on your images
images = ["data/000000000025.jpg"]
pipeline_outputs = yolo_pipeline(images=images)
