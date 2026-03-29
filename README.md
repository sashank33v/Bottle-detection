---
title: Bottle Detection
emoji: 🍾
colorFrom: blue
colorTo: green
sdk: gradio
python_version: "3.10"
sdk_version: "6.10.0"
app_file: app.py
pinned: false
---

# 🍶 Real-Time-Bottle-Detection using YOLOv8

<div align="center">

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/YOLOv8-Ultralytics-FF6B6B?style=for-the-badge">
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
<img src="https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white">
<img src="https://img.shields.io/badge/Roboflow-6706CE?style=for-the-badge">

<br>

<b>A custom YOLOv8 object detection model trained to detect and classify water bottles in real-time</b>

<br>

<a href="#demo">Demo</a> •
<a href="#dataset">Dataset</a> •
<a href="#training">Training</a> •
<a href="#results">Results</a> •
<a href="#quick-start">Quick Start</a>

</div>

---

# 📌 Overview

This project builds a **custom YOLOv8 object detection model** trained to detect water bottles and classify them into two categories.

| Class | Icon | Description |
|------|------|-------------|
| plastic_bottle | 🧴 | Transparent or colored plastic water bottles |
| steel_bottle | 🥤 | Metal or stainless steel water bottles |

The model draws **bounding boxes with confidence scores** around detected bottles in any image or video feed.

---

# 📸 Demo

### After Detection

<div align="center">

<img src="https://jonnadaraju.github.io/Real-Time-Bottle-Detection/images/output.png" width="700">

<p><b>✅ Model detected plastic_bottle and steel_bottle with 0.89 confidence</b></p>

</div>

---

# 🛠️ Tech Stack

| Tool | Purpose |
|-----|---------|
| Python 3.8+ | Programming language |
| YOLOv8 (Ultralytics) | Object detection model |
| Google Colab | Cloud GPU training |
| Roboflow | Dataset preparation and annotation |
| OpenCV | Image processing |
| PyTorch | Deep learning framework |
| Matplotlib | Visualization and charts |

---

# 📊 Dataset

| Detail | Info |
|------|------|
| Source | Roboflow Universe |
| Total Images | 315 |
| Training Set | 250 images |
| Validation Set | 26 images |
| Test Set | 39 images |
| Annotation Format | YOLOv8 Bounding Boxes |
| Input Size | 512×512 |
| Classes | plastic_bottle, steel_bottle |

Dataset link:

dataset/dataset_link.txt

---

# 🏋️ Training

Training was performed on **Google Colab using a Tesla T4 GPU**.

### Training Configuration

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
```

### Training Parameters

| Parameter | Value |
|----------|------|
| Model | YOLOv8 Nano |
| Epochs | 53 |
| Image Size | 640×640 |
| GPU | Tesla T4 |
| Framework | Ultralytics |

---

# 📈 Results

## Performance Metrics

| Metric | Score |
|------|------|
| mAP@50 | 0.806 |
| mAP@50-95 | 0.618 |
| Precision | 0.913 |
| Recall | 0.804 |
| Inference | 43.8 ms |

---

# 📊 Training Charts

<div align="center">

<img src="https://jonnadaraju.github.io/Real-Time-Bottle-Detection/images/overall.png" width="900">

</div>

---

# 🚀 Quick Start

## 1. Clone Repository

```bash
git clone git@github.com:sashank33v/Bottle-detection.git
cd Bottle-detection.git
```

## 2. Install Dependencies

```bash
pip install ultralytics opencv-python matplotlib
```

## 3. Run Detection on Image

```python
from ultralytics import YOLO

model = YOLO("models/best.pt")

results = model.predict(
    source="images/demo/input_plastic.jpg",
    save=True,
    conf=0.5
)

print(f"Detected: {len(results[0].boxes)} bottles")
```

## 4. Run Webcam Detection

```python
from ultralytics import YOLO

model = YOLO("models/best.pt")

model.predict(
    source=0,
    show=True,
    conf=0.5
)
```

## 5. Run Video Detection

```python
from ultralytics import YOLO

model = YOLO("models/best.pt")

model.predict(
    source="your_video.mp4",
    save=True,
    conf=0.5
)
```

---

# 🌐 Deployment

## Best Option: Hugging Face Spaces

This repo is already structured for a **Gradio Space**, which is the cleanest deployment target for a small computer-vision demo:

- Native support for Gradio apps
- Simple model-file hosting directly in the repo
- Free public hosting for demos
- No custom web server setup needed

### Deploy Steps

1. Create a new **Hugging Face Space**
2. Select **Gradio SDK**
3. Upload this repository
4. Keep `app.py` as the entrypoint
5. Ensure `requirements.txt` is included

The metadata block at the top of this `README.md` is already compatible with Spaces.

## Docker Fallback For Render / Railway / VPS

The repo now also includes production container config for generic hosts, which is the best fallback when Spaces scheduling is unreliable.

Build and run locally:

```bash
docker build -t bottle-detection .
docker run -p 7860:7860 bottle-detection
```

The app binds to `0.0.0.0` and reads the `PORT` environment variable, so it works on platforms such as Render and Railway without code changes.

## Render

This repo includes `render.yaml` and can be deployed as a Docker web service.

- Root directory: repository root
- Runtime: Docker
- Health check path: `/`

## Railway

This repo includes `railway.json` and works with the included `Dockerfile`.

- Service type: Docker
- Start command: provided by `Dockerfile`
- Port: provided through the `PORT` environment variable

---

# 🧠 Skills Demonstrated

Computer Vision  
Object Detection  
YOLOv8  
Deep Learning  
Dataset Annotation  
Model Training  
Model Inference  
Python  
Google Colab  
Roboflow  
PyTorch  
OpenCV  
Transfer Learning  

---

<div align="center">

Made with ❤️ using YOLOv8 + Google Colab  

⭐ Star this repo if you found it helpful!

</div>
