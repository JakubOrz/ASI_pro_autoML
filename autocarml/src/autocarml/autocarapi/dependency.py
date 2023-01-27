from typing import Iterable

from kedro.pipeline import Pipeline
from autocarml.src.autocarml.pipelines.wczytywanie_modelu import create_pipeline

# Jeszcze dodać aby data dict się wczytał i będzie spoko

def load_pipeline() -> Iterable[Pipeline]:
    yield create_pipeline()
