import pandas as pd
from typing import Any, Dict, Set
from fastapi import APIRouter, Depends
from ..depends import load_predict_pipeline
from ..schemas import CarStats, PredictionResult
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.runner import SequentialRunner

router = APIRouter()


@router.post("/")
async def predict(carData: CarStats, pipeline: Pipeline = Depends(load_predict_pipeline)) -> PredictionResult:
    dataframe = pd.DataFrame([carData.dict()])

    catalog = DataCatalog(feed_dict={
        "test_data_1": dataframe,
        "model_path": "../data/03_models/pycaret_model_3"

    })
    runner = SequentialRunner(is_async=True)

    success = True
    result = {}
    errors = ""
    try:
        result = runner.run(pipeline=pipeline, catalog=catalog)
        print(f"Rezultat pipeline {result}")
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
