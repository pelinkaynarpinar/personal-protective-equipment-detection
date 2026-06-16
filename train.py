from ultralytics import YOLO

DATASET_YAML_PATH = "dataset/data.yaml"

model = YOLO("yolov8n.pt")

results = model.train(
    data=DATASET_YAML_PATH,
    epochs=25,
    imgsz=640,
    batch=16,
    name="ppe_detection_yolov8"
)
