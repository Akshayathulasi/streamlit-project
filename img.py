from diffusers import StableDiffusionPipeline
import torch

model = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32
)

prompt = "A futuristic city at night"

image = model(prompt).images[0]

image.show()