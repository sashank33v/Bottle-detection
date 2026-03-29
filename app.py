import os
import gradio as gr
from ultralytics import YOLO
from PIL import Image
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="sashank33/bottle_detection_app",
    filename="best.pt"
)
model = YOLO(model_path)

def detect_bottles(image):
    results = model(image)
    result_image = results[0].plot()
import cv2

return Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))

demo = gr.Interface(
    fn=detect_bottles,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="Bottle Detection"
)

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
