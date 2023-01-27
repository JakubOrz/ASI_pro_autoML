from typing import Any, Dict

from fastapi import APIRouter, Depends
from dependency import load_pipeline
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.runner import SequentialRunner
import pandas as pd
from schemas import Emp


router = APIRouter()


@router.get("/")
def main(pipeline: Pipeline = Depends(load_pipeline)) -> Dict[str, Any]:
    print(pipeline)
    catalog = DataCatalog(feed_dict={"xs": [1, 2, 3]})
    runner = SequentialRunner()
    return runner.run(pipeline=pipeline, catalog=catalog)


# @router.post("/worker")
# def emp(employee: Emp, pipeline: Pipeline = Depends(load_pipeline)):
#     pd_frame = pd.DataFrame([employee.dict()])
#     print(pd_frame)
#     es = list(employee)
#     pd.DataFrame(map(lambda e: e.dict(), es))

