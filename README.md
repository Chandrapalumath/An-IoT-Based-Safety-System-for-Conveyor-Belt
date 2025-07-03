# An IoT-Based Safety System for Conveyor Belt 🔧🔥

This project is an intelligent safety system for industrial conveyor belts. It integrates **IoT sensors**, **object detection (YOLOv8)**, and real-time monitoring to prevent hazardous incidents during coal or material transportation.

## 🚀 Features

- 🔥 **Temperature Monitoring**: Detects overheating or fire risk using MLX90640 thermal sensors.
- 🧲 **Metal Detection**: Identifies buried foreign metals using custom sensors built with the TDA0161 IC.
- 🧠 **Foreign Object Detection (YOLOv8)**: Trained on a custom dataset of 17,000+ annotated images to detect unwanted objects on the belt.
- 📶 **Live Web Dashboard**: Shows real-time sensor data and alert notifications via a modern UI.
- 📱 **Mobile-Compatible Alerts**: Push notifications for critical temperature or object detections.

## 🛠️ Technologies Used

| Component          | Stack/Tool                  |
|-------------------|-----------------------------|
| Object Detection   | YOLOv8 + Custom Dataset      |
| Temperature Sensor | MLX90640 IR Thermal Camera   |
| Metal Detection    | TDA0161 Proximity IC         |
| Backend            | Python + HTTP server         |
| Frontend (Web)     | HTML/CSS/JS (or React)       |
| Database           | PostgreSQL (or alternative)  |
| Deployment         | Raspberry Pi                 |



## 🖼️ Dataset

- **17,000+ images**, labeled as `foreign_object`.
- Split into `train/` and `val/` directories.
- Label format: YOLO format (.txt files with class & bbox)

## 📊 Model Performance
| Metric         | Value |
|----------------|-------|
| Precision      | 0.76  |
| Recall         | 0.65  |
| mAP@0.5        | 0.71  |
| mAP@0.5:0.95   | 0.29  |


