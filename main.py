import yaml
from llm.planner import plan
from models.config import Config
from vision.image import generate_image
from vision.video import image_to_video_generator

config: Config = yaml.safe_load(open("config.yaml"))
prompt: str = input("Describe your video: ")

plan_data = plan(prompt, config)

for scene in plan_data["scenes"]:
  image = generate_image(scene["image_prompt"], "output/images")
  video = image_to_video_generator(image, "output/videos")
  
print("✅ Video created: output/final.mp4")