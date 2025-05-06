from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class Token(BaseModel):
    success: str
    api_token: str

# Модель для одной пивоварни
class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: Optional[str]
    postal_code: str
    country: str
    longitude: Optional[str]
    latitude: Optional[str]
    phone: Optional[str]
    website_url: Optional[HttpUrl]
    state: str
    street: Optional[str]



# Модель для списка пивоварен
class ListBrewery(BaseModel):
    message: List[Brewery]

# Модель для одной пивоварни
class SingleBrewery(BaseModel):
    message: Brewery