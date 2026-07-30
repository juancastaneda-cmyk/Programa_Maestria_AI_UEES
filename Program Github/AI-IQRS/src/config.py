from pathlib import Path

# ============================================
# Project Paths
# ============================================

ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = ROOT / "models" / "best.pt"

# ============================================
# Camera Configuration
# ============================================

CAMERA_INDEX = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# ============================================
# YOLO Configuration
# ============================================

CONFIDENCE = 0.30

IMAGE_SIZE = 1024