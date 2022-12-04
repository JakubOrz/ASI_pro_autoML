"""
This is a boilerplate pipeline 'optuna_model_training'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from ..pycret_pipeline.nodes import preprocess_dates
from .nodes import get_optunised_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_dates,
            inputs="small_raw_car_data_path",
            outputs="cleared_dates",
            name="Clear_dates"
        ),
        node(
            func=get_optunised_model,
            inputs=["cleared_dates", "params:train_target", "params:n_iter"],
            outputs="trained_optunised_model",
            name="Get_best_optuna_model"
        )
    ])
