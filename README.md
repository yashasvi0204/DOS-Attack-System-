# DOS Attack Detection

Detect Denial-of-Service (DoS) attacks using threshold-based and anomaly-based methods (Isolation Forest).
This repository contains preprocessing, training, evaluation and a simple realtime monitor demo.

## Quick start
1. Create a Python virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Place CICDDoS2019 CSV files into `data/raw/`.
3. Run preprocessing:

```bash
bash scripts/run_preprocessing.sh
```

4. Train models:

```bash
bash scripts/run_train.sh
```

5. Run the realtime monitor (simulated or live input):

```bash
bash scripts/run_realtime.sh
```
