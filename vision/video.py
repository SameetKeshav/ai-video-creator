import torch, os, uuid, imageio
from diffusers import StableVideoDiffusionPipeline
from PIL import Image

pipe = StableVideoDiffusionPipeline.from_pretrained(
  "stabilityai/stable-video-diffusion-img2vid",
  torch_dtype=torch.float16
).to("mps")

def image_to_video_generator(image_path, out_dir) -> str:
  print("Generating video")
  os.makedirs(out_dir, exist_ok=True)
  image = Image.open(image_path).convert("RGB")
  
  frames = pipe(
    image,
    num_frames=16,
    decode_chunk_size=4
  ).frames[0]
  
  out_path = f"{out_dir}/{uuid.uuid4()}.mp4"
  imageio.mimsave(out_path, frames, fps=8)
  
  return out_path
  