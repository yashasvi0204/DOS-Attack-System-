# utils.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path

def save_model(obj, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(obj, path)

def load_model(path: Path):
    return joblib.load(path)

def train_test_split_df(df: pd.DataFrame, target: str = "Label", test_size=0.2, random_state=42):
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
