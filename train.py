# train.py
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
from .config import PROCESSED_DIR, MODELS_DIR, RANDOM_STATE
from .utils import train_test_split_df, save_model

def train_isolation_forest():
    df = pd.read_csv(Path(PROCESSED_DIR) / 'processed.csv')
    benign = df[df['Label'] == 0]
    X_benign = benign.drop(columns=['Label'])

    iso = IsolationForest(random_state=RANDOM_STATE, n_estimators=100, contamination=0.05)
    iso.fit(X_benign)

    Path(MODELS_DIR).mkdir(parents=True, exist_ok=True)
    save_model(iso, Path(MODELS_DIR) / 'isolation_forest.joblib')
    print('Trained and saved IsolationForest')

if __name__ == '__main__':
    train_isolation_forest()
