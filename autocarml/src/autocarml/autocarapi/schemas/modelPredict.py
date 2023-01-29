from typing import Any, Dict, Optional

from pydantic import BaseModel


class ModelPredict(BaseModel):
    isSuccess: bool
    errors: Optional[str]
    result: Optional[Dict[str, float]]
