import pickle
import uvicorn
import numpy as np
from fastapi import FastAPI
from sklearn.linear_model import Ridge

from models import CarStats


app = FastAPI()
ml_model: Ridge = pickle.load(open('../ml_models/pycarret_model_1.pkl', 'rb'))


@app.get("/")
def index():
    return "Hello index"


@app.get("/model")
def model():
    return "Here will be our model"


@app.get("/model_inputs")
def testModel():
    return ml_model.n_features_in_


@app.post("/predict")
def predict(data: CarStats):
    try:
        np_data = np.array([x for x in data.dict().values()])
        prediction = ml_model.predict(np_data)
        return {
            "Succes": True,
            "Result": prediction
        }
    except Exception as ex1:
        return {
            "Succes": False,
            "Error": str(ex1)
        }


if __name__ == '__main__':
    uvicorn.run("fastApi:app", host="127.0.0.1", port=5000, log_level="info")
