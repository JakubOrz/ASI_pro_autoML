import joblib
import uvicorn
import pandas as pd
from fastapi import FastAPI, Depends
from pycaret.regression import predict_model

from models import CarStats


# Should load model from container volume
def load_model():
    yield joblib.load('/home/jakub/PycharmProjects/ASI_pro_autoML/autocar_API/ml_models/pycaret_best_model_2.pkl')


app = FastAPI()


@app.get("/")
def index():
    return "Hello index"


@app.get("/model")
def model():
    return "Here will be our model"


@app.get("/model_inputs")
def testModel(mlModel=Depends(load_model)):
    return mlModel.n_features_in_


@app.post("/dataframe")
def predict(data: CarStats):
    query = pd.DataFrame([data.dict()])
    print(query)
    return {'dataframe': str(query)}


@app.post("/predict")
def predict(data: CarStats, mlModel=Depends(load_model)):
    try:
        query = pd.DataFrame([data.dict()])
        print(query)
        print(mlModel.predict(query))
        return {'prediction': "Poczekaj sobie"}
    except Exception as ex1:
        return {
            "Succes": False,
            "Error": str(ex1)
        }


if __name__ == '__main__':
    uvicorn.run("fastApi:app", host="127.0.0.1", port=5000, log_level="info")
