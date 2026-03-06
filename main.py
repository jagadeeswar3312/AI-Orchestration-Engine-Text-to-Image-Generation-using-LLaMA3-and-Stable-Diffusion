# install: pip install huggingface_hub python-dotenv gradio ollama

import gradio as gr
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from summary import generate_prompt

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
IMAGE_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

image_client = InferenceClient(model=IMAGE_MODEL, token=HF_TOKEN)

def pipeline(text):
    enhanced_prompt = generate_prompt(text)
    image = image_client.text_to_image(enhanced_prompt)
    return enhanced_prompt, image

demo = gr.Interface(
    fn=pipeline,
    inputs=gr.Textbox(lines=8, label="Enter Rough Text"),
    outputs=[
        gr.Textbox(label="Generated Image Prompt"),
        "image"
    ],
    title="AI Orchestration Engine",
    description="Text → Prompt Engineering (Ollama) → Image Generation (Stable Diffusion)"
)

if __name__ == "__main__":
    demo.launch()