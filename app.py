import os
from pathlib import Path

import gradio as gr
from PIL import Image
from ultralytics import YOLO

MODEL_PATH = Path("models/best.pt")
EXAMPLE_IMAGES = [
    "images/prediction-1.jpeg",
    "images/webcam-sample.jpeg",
    "images/images (6).jpeg",
]


if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = YOLO(MODEL_PATH)


def detect_bottles(image: Image.Image) -> Image.Image:
    results = model(image)
    result_image = results[0].plot()
    return Image.fromarray(result_image)


demo = gr.Interface(
    fn=detect_bottles,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Image(type="pil", label="Detected Bottles"),
    title="Bottle Detection",
    description="Upload an image to detect plastic and steel bottles using a custom YOLOv8 model.",
    examples=EXAMPLE_IMAGES,
)


if __name__ == "__main__":
    demo.queue().launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", "7860")),
    )
