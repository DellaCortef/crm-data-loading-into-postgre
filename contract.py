from enum import Enum
from typing import Tuple
from datetime import datetime
from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt


class Sales(BaseModel):
    email: EmailStr
    date_time: datetime
    product_value: PositiveFloat
    product_quantity: PositiveInt
    product_type: ProductEnum

    @validate_call('product_type')
    def category_must_be_in_the_enum(cls, v):
        return v

class ProductEnum(str, Enum):
    product1 = "ZapFlow com Gemini"
    product2 = "ZapFlow com chatGPT"
    product3 = "ZapFlow com Llama 3.0"