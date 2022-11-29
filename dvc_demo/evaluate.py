from __future__ import annotations

import json
import pickle

import fire
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


def evaluate():
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)

    test_df = pd.read_csv('data/test.csv')

    y_pred = model.predict(X=test_df.drop(columns=['target']))

    metrics = {
        'mae': mean_absolute_error(y_true=test_df.target, y_pred=y_pred),
        'mse': mean_squared_error(y_true=test_df.target, y_pred=y_pred),
    }

    with open('metrics.json', 'w') as f:
        json.dump(metrics, f)


if __name__ == '__main__':
    fire.Fire(evaluate)
