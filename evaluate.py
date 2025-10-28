# evaluate.py
import pandas as pd
from pathlib import Path
from sklearn.metrics import classification_report, confusion_matrix
from .config import PROCESSED_DIR, MODELS_DIR
from .utils import load_model

def evaluate_isolation_forest():
    df = pd.read_csv(Path(PROCESSED_DIR) / 'processed.csv')
    X = df.drop(columns=['Label'])
    y = df['Label']

    iso = load_model(Path(MODELS_DIR) / 'isolation_forest.joblib')
    preds = iso.predict(X)
    preds = [0 if p == 1 else 1 for p in preds]

    print(classification_report(y, preds, digits=4))
    print('Confusion matrix:\n', confusion_matrix(y, preds))

if __name__ == '__main__':
    evaluate_isolation_forest()
