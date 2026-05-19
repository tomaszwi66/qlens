OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5vl:7b"
TEXT_MODEL_NAME = "qwen2.5:7b"  # for video-frame aggregation (text-only)
INFER_SIZE = 1024
REQUEST_TIMEOUT = 120
OVERLAY_AUTO_CLOSE_MS = 30_000
HOTKEY = "ctrl+shift+a"

# Defaults (overridable via Settings dialog at runtime)
MAX_OBJECTS_DEFAULT = 1
VIDEO_INTERVAL_S_DEFAULT = 0.0  # 0 = continuous (next frame grabbed as soon as previous one is processed)
VIDEO_MAX_FRAMES_DEFAULT = 60
