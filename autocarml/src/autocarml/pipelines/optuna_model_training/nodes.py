"""
This is a boilerplate pipeline 'optuna_model_training'
generated using Kedro 0.18.3
"""
from typing import Any
import pandas
import optuna
from pycaret.regression import setup, create_model, tune_model


def get_optunised_model(data_set: pandas.DataFrame, target: str, n_iter: int) -> Any:
    setup(data=data_set, target=target)
    logistic_regression = create_model('lr')
    tuned_lr = tune_model(
        logistic_regression,
        n_iter=n_iter,
        search_library="optuna",
        search_algorithm="random",
        early_stopping=True,
        choose_better=True
    )
    return tuned_lr
