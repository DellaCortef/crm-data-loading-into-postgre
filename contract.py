from enum import Enum
from typing import Tuple
from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, validator, ValidationError


class ProductEnum(str, Enum):
    product1 = "ZapFlow com Gemini"
    product2 = "ZapFlow com chatGPT"
    product3 = "ZapFlow com Llama 3.0"

class Sales(BaseModel):
    email: EmailStr
    date_time: datetime
    product_value: PositiveFloat
    product_quantity: PositiveInt
    product_type: ProductEnum

    @validator('date_time')
    def validate_date_interval(cls, v):
        # Define the allowed date range
        interval_start = datetime(2024, 9, 1)  # 01/09/2024
        interval_end = datetime(2024, 9, 12, 23, 59, 59)  # 12/09/2024 until 23:59:59

        # Checks if the date is within the allowed range
        if not (interval_start <= v <= interval_end):
            raise ValueError("The date of sale must be between 09/01/2024 and 09/12/2024")
        return v

    @validator('produto')
    def categoria_deve_estar_no_enum(cls, v):
        return v