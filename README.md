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
- 
## Dataset and Credits

The dataset used in this project was downloaded from Roboflow Universe.

**Dataset:** Personal Protective Equipment
**Platform:** Roboflow Universe
**Format:** YOLOv8
**License:** CC BY 4.0

Dataset classes:

* Gloves
* Helmet
* No-Helmet
* No-gloves
* No-vest
* Vest

This project uses the dataset for educational and portfolio purposes. The dataset was used to train a YOLOv8 object detection model for detecting personal protective equipment in workplace images.

The original dataset is not included in this repository. Only the trained model, project code, training results, and sample prediction outputs are provided.

According to the CC BY 4.0 license, appropriate credit is given to the dataset source. Any model training, evaluation, and prediction outputs in this repository were created as part of this project.

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
