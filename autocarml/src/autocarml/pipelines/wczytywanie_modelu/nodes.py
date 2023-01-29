"""
This is a boilerplate pipeline 'wczytywanie_modelu'
generated using Kedro 0.18.4
"""
import pickle
from typing import Any

import pandas
from pycaret.regression import load_model, predict_model
import pandas as pd


def predict(model, data: pd.DataFrame) -> Any:
    predict_data = [[2014, 'BMW', '3 Series', '328i SULEV', 'Sedan', 'automatic', 4.5, 1331.0, 'gray', 'black', 31900]]
    data_frame = pd.DataFrame(predict_data, columns=
    ['year', 'make', 'model', 'trim', 'body', 'transmission', 'condition', 'odometer', 'color', 'interior', 'mmr']
                              )
    result = predict_model(model, data=data_frame)
    # print(result)
    return result
