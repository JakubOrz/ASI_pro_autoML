import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


# old pipeline for tests (it worked at least)
#
# def read_chunk_of_data(data_set: pd.DataFrame, chunk_size: int) -> pd.DataFrame:
#    return data_set[:chunk_size+1]


# def print_data_frame_head(data_frame: pd.DataFrame) -> None:
#    print(data_frame.head())


# def get_yearly_sales_cout(data_frame: pd.DataFrame):
#    result_df = data_frame.groupby(["year"])["year"].count()
#    result_dict = {int(x): int(result_df[x]) for x in result_df.keys()}
#    print(result_dict)
#    return result_dict

def split_data_set(data_set: pd.DataFrame):
    data = data_set[["symboling", "wheelbase", "carlength",
                     "carwidth", "carheight", "curbweight",
                     "enginesize", "boreratio", "stroke",
                     "compressionratio", "horsepower", "peakrpm",
                     "citympg", "highwaympg", "price"]]
    x = np.array(data.drop(["price"], 1))
    y = np.array(data["price"])

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

    return xtrain, xtest, ytrain, ytest


def create_model(xtrain, ytrain):
    model = DecisionTreeRegressor()
    model.fit(xtrain, ytrain)
    return model


def predict_and_score(model, xtest):
    predictions = model.predict(xtest)
    print(model.score(xtest, predictions))
