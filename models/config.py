from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class LlmConfig:
    provider: str
    base_url: str
    model: str
    temperature: float
    max_tokens: int

@dataclass
class VideoConfig:
    width: int
    height: int
    frames: int
    fps: int

@dataclass
class Config:
    llm: LlmConfig
    video: VideoConfig
