from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class Token(BaseModel):
    success: str
    api_token: str

class AddCart(BaseModel):
    success: str

class UpdateCart(BaseModel):
    success: str

class DeleteCart(BaseModel):
    success: str

class Product(BaseModel):
    cart_id: str
    product_id: str
    name: str
    model: str
    option: List
    quantity: str
    stock: bool
    shipping: str
    price: str
    total: str
    reward: int


class Total(BaseModel):
    title: str
    text: str


class SelectCart(BaseModel):
    products: List[Product]
    vouchers: List
    totals: List[Total]

class CurrencyChange(BaseModel):
    success: str

class AddVoucher(BaseModel):
    success: str
