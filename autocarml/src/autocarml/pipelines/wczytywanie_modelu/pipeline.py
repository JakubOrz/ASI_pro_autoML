"""
This is a boilerplate pipeline 'wczytywanie_modelu'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import *


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=import_model,
            inputs=[],
            outputs='model',
            name="Imported_model"
        ),
        node(
            func=predict,
            inputs="model",
            outputs='result',
            name= "Prediction"
        )
    ])
