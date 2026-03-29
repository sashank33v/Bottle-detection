import gradio as gr
from ultralytics import YOLO
from PIL import Image
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="sashank33v/bottle-detection",
    filename="best.pt"
)
model = YOLO(model_path)


def detect_bottles(image):
    results = model(image)
    result_image = results[0].plot()
    return Image.fromarray(result_image)


demo = gr.Interface(
    fn=detect_bottles,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Image(type="pil", label="Detected Bottles"),
    title="🍾 Bottle Detection",
    description="Upload an image to detect bottles using YOLOv8"
)

import os

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
