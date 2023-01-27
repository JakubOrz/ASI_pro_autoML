"""
This is a boilerplate pipeline 'pycret_pipeline'
generated using Kedro 0.18.3
"""
from typing import Tuple, Any
import pandas
from pycaret.regression import setup
from pycaret.regression import compare_models, evaluate_model


def preprocess_dates(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    data_frame['saledate'] = pandas.to_datetime(data_frame['saledate'], utc=True)
    return data_frame


def show_dtypes(data_frame: pandas.DataFrame) -> None:
    print(data_frame.dtypes)
    return


def show_head(data_frame: pandas.DataFrame) -> None:
    print(data_frame.head())
    return


def create_model_setup(data_frame: pandas.DataFrame, target: str) -> Tuple[Any, ...]:
    model_setup = setup(data=data_frame, target=target)
    return model_setup


def generate_model(data_frame: pandas.DataFrame, target: str) -> Any:
    setup(data=data_frame, target=target)
    best = compare_models(sort="TT")
    print(best)
    return best


