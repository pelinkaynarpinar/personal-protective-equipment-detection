from ultralytics import YOLO

MODEL_PATH = "weights/best.pt"
SOURCE_PATH = "sample_images"

model = YOLO(MODEL_PATH)

results = model.predict(
    source=SOURCE_PATH,
    conf=0.32,
    imgsz=1280,
    iou=0.45,
    show_conf=False,
    save=True
)
