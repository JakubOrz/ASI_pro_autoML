from datetime import datetime
from pydantic import BaseModel


class CarStats(BaseModel):
    year: int
    car_brand: str
    car_model: str
    trim: str
    body_type: str
    transmission_type: str
    vin_numer: str
    state: str
    condition: float
    odometer: int
    color: str
    interior: str
    seller_name: str
    mmr: int
    sale_time: datetime
