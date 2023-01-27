"""
This is a boilerplate pipeline 'pycret_pipeline'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import *


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_dates,
            inputs="small_raw_car_data_path",
            outputs="cleared_dates",
            name="Clear_dates"
        ),
        node(
            func=generate_model,
            inputs=["cleared_dates", "params:train_target"],
            outputs="trained_model",
            name="Get_best_model"
        )
    ])
