import os, torch, uuid
from diffusers import StableDiffusionXLPipeline

pipe = StableDiffusionXLPipeline.from_pretrained(
  "stabilityai/stable-diffusion-xl-base-1.0",
  torch_dtype=torch.float32,
  variant=None
)

pipe.to("mps")
pipe.enable_attention_slicing()
pipe.enable_vae_slicing()
pipe.enable_vae_tiling()

def generate_image(prompt, out_dir) -> str:
  print("Generating Images")
  os.makedirs(out_dir, exist_ok=True)
  
  image = pipe(
    prompt=prompt,
    num_inference_steps=30,
    guidance_scale=7.5
  ).images[0]
  
  path = f"{out_dir}/{uuid.uuid4()}.png"
  image.save(path)
  return path