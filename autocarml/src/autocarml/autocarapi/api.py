import uvicorn
from fastapi import FastAPI, Depends
from typing import Dict, Iterable
from kedro.pipeline import Pipeline
from dependency import load_pipeline
from router import router

app = FastAPI()
app.include_router(router, prefix="/dataprocesing")


if __name__ == '__main__':
    uvicorn.run("api:app", host="127.0.0.1", port=7200, log_level="info")