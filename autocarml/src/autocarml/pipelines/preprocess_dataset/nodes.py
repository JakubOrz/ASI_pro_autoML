import pandas as pd


def read_chunk_of_data(data_set: pd.DataFrame, chunk_size: int) -> pd.DataFrame:
    return data_set[:chunk_size+1]


def print_data_frame_head(data_frame: pd.DataFrame) -> None:
    print(data_frame.head())


def get_yearly_sales_cout(data_frame: pd.DataFrame):
    result_df = data_frame.groupby(["year"])["year"].count()
    result_dict = {int(x): int(result_df[x]) for x in result_df.keys()}
    print(result_dict)
    return result_dict
