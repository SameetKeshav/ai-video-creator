import requests
import json
from models.config import Config

def plan(prompt: str, config: Config):
  url: str = f"{config["llm"]["base_url"]}/chat/completions"
  headers = {
        "Content-Type": "application/json"
    }
  payload = {
    "model": config["llm"]["model"],
    "temperature": config["llm"]["temperature"],
    "max_tokens": config["llm"]["max_tokens"],
    "messages": [
      {
        "role": "system",
        "content": (
          "You are a video director. "
          "Convert ideas into short video scene plans."
        )
      },
      {
        "role": "user",
        "content": f"""
          Return JSON ONLY in this format:
          {{
          "scenes": [
            {{
              "image_prompt": "cinematic description",
              "narration": "voiceover text"
            }}
          ]
        }}
        Idea:
        {prompt}
        """
      }
    ]
  }
  
  response = requests.post(url, json=payload)
  response.raise_for_status()
  
  content = response.json()["choices"][0]["message"]["content"]
  return json.loads(content)