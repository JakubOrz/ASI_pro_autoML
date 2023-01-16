"""
This is a boilerplate pipeline 'pycaret_2'
generated using Kedro 0.18.3
"""

from typing import Tuple, Any
import pandas
from pycaret.regression import setup
from pycaret.regression import create_model
from pycaret.regression import compare_models, evaluate_model

def preprocess_dates(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    data_frame['saledate'] = pandas.to_datetime(data_frame['saledate'], utc=True)
    data_frame.drop(columns=["vin", "state", "seller", "saledate"], inplace=True)
    data_frame = data_frame.drop(labels=range(100000, 558811), axis=0)
    return data_frame


def show_dtypes(data_frame: pandas.DataFrame) -> None:
    print(data_frame.dtypes)
    return


def show_head(data_frame: pandas.DataFrame) -> None:
    print(data_frame.head())
    return


def create_model_setup(data_frame: pandas.DataFrame, target: str) -> Tuple[Any, ...]:
    model_setup = setup(data=data_frame, target=target, use_gpu=True)
    return model_setup

def generate_model(data_frame: pandas.DataFrame, target: str) -> Any:
    setup(data=data_frame, target=target)
    best_2 = create_model('dt')
    print(best_2)
    return best_2