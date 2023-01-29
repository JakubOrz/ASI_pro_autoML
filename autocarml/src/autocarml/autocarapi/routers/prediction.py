import os
import pickle

import pandas as pd
from typing import Any, Dict, Set
from fastapi import APIRouter, Depends
from ..depends import load_predict_pipeline
from ..schemas import CarStats, PredictionResult
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.runner import SequentialRunner
from pycaret.regression import load_model

router = APIRouter()


@router.post("/")
def predict(carData: CarStats, pipeline: Pipeline = Depends(load_predict_pipeline)) -> PredictionResult:
    model = load_model("../data/03_models/pycaret_best_model_2")
    dataframe = pd.DataFrame([carData.dict()])

    catalog = DataCatalog(feed_dict={
        "test_data_1": pd.DataFrame([carData.dict()]),
        "trained_model_2": model

    })
    runner = SequentialRunner()
    success = True
    result = {}
    errors = ""
    try:
        result = runner.run(pipeline=pipeline, catalog=catalog)
        print(result)
        success: bool = True
        errors: str = ""
    except Exception as ex1:
        result = None
        success = False
        errors = str(ex1)
    finally:
        return PredictionResult(
            isSuccess=success,
            errors=errors,
            result=result
        )


@router.get("/test")
def test_pipeline(pipeline: Pipeline = Depends(load_predict_pipeline)) -> str:
    return pipeline.to_json()


@router.get("/describe")
def describe(pipeline: Pipeline = Depends(load_predict_pipeline)) -> str:
    return pipeline.describe()


@router.get("/inputs")
def inputs(pipeline: Pipeline = Depends(load_predict_pipeline)) -> Set[str]:
    return pipeline.all_inputs()


@router.get("/outputs")
def inputs(pipeline: Pipeline = Depends(load_predict_pipeline)) -> Set[str]:
    return pipeline.all_outputs()
