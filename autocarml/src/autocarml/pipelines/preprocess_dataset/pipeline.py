"""
This is a boilerplate pipeline 'preprocess_dataset'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
#from .nodes import read_chunk_of_data, print_data_frame_head, get_yearly_sales_cout
from .nodes import split_data_set, create_model, predict_and_score

# def create_pipeline(**kwargs) -> Pipeline:
#     return pipeline([
#         node(
#             func=read_chunk_of_data,
#             inputs=["small_raw_car_data_path", "params:chunk_size"],
#             outputs="car_data_chunk",
#             name="Read_chunk_of_data"
#         ),
#         node(
#             func=print_data_frame_head,
#             inputs="car_data_chunk",
#             outputs=None,
#             name="Print_data_chunk_head"
#             ),
#         node(
#             func=get_yearly_sales_cout,
#             inputs="small_raw_car_data_path",
#             outputs="yearly_sales",
#             name="Get_yearly_sales"
#         )
#     ])

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data_set,
            inputs=["small_raw_car_data_path"],
            outputs=["xtrain","xtest","ytrain","ytest"],
            name="Split_data_set"
        ),
        node(
            func=create_model,
            inputs=["xtrain", "ytrain"],
            outputs="model",
            name="Create_model"
            ),
        node(
            func=predict_and_score,
            inputs=["model","xtest"],
            outputs=None,
            name="Predict_and_score"
        )
    ])