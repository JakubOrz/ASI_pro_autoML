from pydantic import BaseModel


class CarStats(BaseModel):
    year: int
    car_brand: str
    car_model: str
    trim: str
    body_type: str
    transmission_type: str
    condition: float
    odometer: int
    color: str
    interior: str
    mmr: int
