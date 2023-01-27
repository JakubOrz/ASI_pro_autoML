"""
This is a boilerplate pipeline 'wczytywanie_modelu'
generated using Kedro 0.18.4
"""
from typing import Any

import pandas
from pycaret.regression import load_model, predict_model
import pandas as pd


def import_model() -> pd.DataFrame:
    model = load_model('./data/03_models/pycaret_best_model_2')
    return model


def predict(model: pd.DataFrame) -> Any:
    #
    predict_data = [[2014, 'BMW', '3 Series', '328i SULEV', 'Sedan', 'automatic', 4.5, 1331.0, 'gray', 'black', 31900]]
    #
    data_frame = pd.DataFrame(predict_data,
                              columns=['year', 'make', 'model', 'trim', 'body', 'transmission', 'condition',
                                       'odometer', 'color', 'interior', 'mmr'])
    result = predict_model(model, data=data_frame)
    print(result)
    return result
