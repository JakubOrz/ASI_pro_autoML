from pydantic import BaseModel


class CarStats(BaseModel):
    year: int
    make: str
    model: str
    trim: str
    body: str
    transmission: str
    condition: float
    odometer: int
    color: str
    interior: str
    mmr: int
