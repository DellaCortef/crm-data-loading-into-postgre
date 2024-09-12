from typing import Tuple
from datetime import datetime
from pydantic import BaseModel, EmailStr


class Sales(BaseModel):
    email: EmailStr
    date_time: datetime
    product_value: float
    product_quantity: int
    product_type: str