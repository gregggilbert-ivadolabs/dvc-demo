from __future__ import annotations

import fire
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


def process():
    ds = fetch_california_housing(as_frame=True, return_X_y=True)
    df = pd.concat([ds[0], ds[1].rename('target')], axis=1)
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=1234)
    train_df.to_csv('data/train.csv', index=False)
    test_df.to_csv('data/test.csv', index=False)


if __name__ == '__main__':
    fire.Fire(process)
