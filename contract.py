from typing import Tuple
from datetime import datetime
from pydantic import BaseModel


class Sales(BaseModel):
    email: str
    date_time: datetime
    product_value: float
    product_quantity: int
    product_type: str