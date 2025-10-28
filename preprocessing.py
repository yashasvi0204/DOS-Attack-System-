# preprocessing.py
import pandas as pd
from pathlib import Path
from .config import RAW_DIR, PROCESSED_DIR

def load_raw_csvs(raw_dir=RAW_DIR):
    files = list(Path(raw_dir).glob("*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSVs found in {raw_dir}")
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

def basic_cleaning(df: pd.DataFrame):
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df

def create_features(df: pd.DataFrame):
    if 'Packet Count' in df.columns and 'Flow Duration' in df.columns:
        df['pkt_rate'] = df['Packet Count'] / (df['Flow Duration'] + 1e-6)
    return df

def preprocess_and_save():
    df = load_raw_csvs()
    df = basic_cleaning(df)
    df = create_features(df)
    Path(PROCESSED_DIR).mkdir(parents=True, exist_ok=True)
    out = Path(PROCESSED_DIR) / 'processed.csv'
    df.to_csv(out, index=False)
    print('Saved processed to', out)

if __name__ == '__main__':
    preprocess_and_save()
