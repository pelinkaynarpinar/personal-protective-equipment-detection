# Personal Protective Equipment Detection

This project is a computer vision application for detecting personal protective equipment in workplace images using YOLOv8.

The model detects safety-related classes such as helmets, vests, gloves, and missing equipment conditions.

## Project Purpose

The aim of this project is to support workplace safety by detecting whether workers are wearing required personal protective equipment.

## Classes

The model was trained on the following classes:

- Gloves
- Helmet
- No-Helmet
- No-gloves
- No-vest
- Vest

## Technologies Used

- Python
- YOLOv8
- Ultralytics
- OpenCV
- Roboflow
- Google Colab

## Model Performance

Final validation results:

| Metric | Value |
|---|---:|
| Precision | 0.715 |
| Recall | 0.755 |
| mAP50 | 0.754 |
| mAP50-95 | 0.418 |

## Results

Training results and prediction examples are available in the `results/` folder.

## Project Structure

```text
personal-protective-equipment-detection/
│
├── README.md
├── requirements.txt
├── train.py
├── predict.py
│
├── weights/
│   └── best.pt
│
├── results/
│   ├── training_results.png
│   ├── confusion_matrix.png
│   └── prediction_images/
│
└── dataset/
    └── README.md
```

## How to Run Prediction

Install the required packages:

```bash
pip install -r requirements.txt
```

Put test images into a folder named `sample_images`.

Then run:

```bash
python predict.py
```

The predicted images will be saved automatically by YOLO.

## Notes

The model performs better on helmet and vest detection. Glove detection is less stable because gloves are small objects and may appear partially occluded.

## Author

Pelin Kaynarpınar
