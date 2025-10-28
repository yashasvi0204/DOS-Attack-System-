# config.py
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = ROOT / "models"

# training params
RANDOM_STATE = 42
BATCH_SIZE = 64
NUM_EPOCHS = 20
LR = 1e-3

# thresholds (example defaults)
DEFAULT_PKT_RATE_THRESHOLD = 1000  # packets per second
