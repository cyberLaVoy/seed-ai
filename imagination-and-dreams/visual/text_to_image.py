import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
# Define the denoising scheuler
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
# Move pipe to GPU
pipe = pipe.to("cuda")

# For GPUs with low VRAM
pipe.enable_attention_slicing()

prompt = "An android dreaming of electric sheep."

num_images = 8

for i in range(num_images):
    image = pipe(prompt, height=768, width=768).images[0]
    image.save(str(i)+".png")

