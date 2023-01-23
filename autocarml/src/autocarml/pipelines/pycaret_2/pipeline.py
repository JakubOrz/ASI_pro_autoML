"""
This is a boilerplate pipeline 'pycaret_2'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import *


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_dates,
            inputs="large_raw_car_data_path",
            outputs="cleared_dates_2",
            name="Clear_dates_2"
        ),
        node(
            func=generate_model,
            inputs=["cleared_dates_2", "params:train_target"],
            outputs="trained_model_2",
            name="Get_best_model_2"
        )
    ])
