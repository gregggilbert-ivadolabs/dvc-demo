from __future__ import annotations

import pickle

import fire
import pandas as pd
from sklearn.neural_network import MLPRegressor
from utils import load_yaml


def train():
    conf = load_yaml('params.yaml')['model']
    model = MLPRegressor(
        solver='lbfgs',
        alpha=1e-5,
        hidden_layer_sizes=(
            conf['num_hidden_layer'],
            conf['hidden_layer_size'],
        ),
        random_state=1234,
    )
    train_df = pd.read_csv('data/train.csv')
    model.fit(X=train_df.drop(columns=['target']), y=train_df.target)

    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    fire.Fire(train)
