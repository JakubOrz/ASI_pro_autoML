"""
This is a boilerplate pipeline 'wczytywanie_modelu'
generated using Kedro 0.18.4
"""
import pickle
from typing import Any

from pycaret.regression import load_model, predict_model
import pandas as pd


def predict(model_path: str, data: pd.DataFrame) -> float:
    predict_data = [[2014, 'BMW', '3 Series', '328i SULEV', 'Sedan', 'automatic', 4.5, 1331.0, 'gray', 'black', 31900]]
    data_frame = pd.DataFrame(predict_data, columns=
    ['year', 'make', 'model', 'trim', 'body', 'transmission', 'condition', 'odometer', 'color', 'interior', 'mmr']
                              )
    model = load_model(model_path)
    result_df = predict_model(model, data=data)
    result = result_df.iloc[0]['Label']
    return result
