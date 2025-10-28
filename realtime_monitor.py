# realtime_monitor.py
"""Simple realtime monitor: reads a CSV stream (appended to) and triggers alerts based on threshold and IsolationForest."""
import time
import pandas as pd
from pathlib import Path
from .config import PROCESSED_DIR, MODELS_DIR, DEFAULT_PKT_RATE_THRESHOLD
from .utils import load_model

MODEL_PATH = Path(MODELS_DIR) / 'isolation_forest.joblib'

def simple_threshold_check(row):
    return row.get('pkt_rate', 0) > DEFAULT_PKT_RATE_THRESHOLD

def run_monitor(stream_csv: Path, poll_interval=2.0):
    iso = None
    if MODEL_PATH.exists():
        iso = load_model(MODEL_PATH)
    seen = 0
    print('Starting monitor. Watching', stream_csv)
    while True:
        if not Path(stream_csv).exists():
            time.sleep(poll_interval)
            continue
        df = pd.read_csv(stream_csv)
        new = df.iloc[seen:]
        for _, row in new.iterrows():
            if simple_threshold_check(row):
                print('THRESHOLD ALERT:', row.to_dict())
            if iso is not None:
                x = row.drop(labels=['Label'], errors='ignore').values.reshape(1, -1)
                score = iso.predict(x)[0]
                if score == -1:
                    print('ANOMALY ALERT:', row.to_dict())
        seen = len(df)
        time.sleep(poll_interval)

if __name__ == '__main__':
    run_monitor(Path(PROCESSED_DIR) / 'live_stream.csv')
