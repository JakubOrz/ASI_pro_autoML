"""
This is a boilerplate pipeline 'testowa_do_nauki'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import say_hi


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=say_hi,
            inputs="params:key1",
            outputs="output1",
            name="Say_hi"
        ),
        node(
            func=say_hi,
            inputs="output1",
            outputs="output2",
            name="Say_hi_2"
        )
    ])
