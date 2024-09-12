from enum import Enum
from typing import Tuple
from datetime import datetime
from pydantic import BaseModel, EmailStr, validate_call


class Sales(BaseModel):
    email: EmailStr
    date_time: datetime
    product_value: float
    product_quantity: int
    product_type: ProductEnum

class ProductEnum(str, Enum):
    product1 = "ZapFlow com Gemini"
    product2 = "ZapFlow com chatGPT"
    product3 = "ZapFlow com Llama 3.0"