import torch
from diffusers import StableDiffusionPipeline

model_id = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# For GPUs with low VRAM
# pipe.enable_attention_slicing()

prompt = "electric sheep"
image = pipe(prompt).images[0]
    
image.save("an_androids_dream_slice.png")

