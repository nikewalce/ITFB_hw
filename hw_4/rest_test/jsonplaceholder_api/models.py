from pydantic import BaseModel
from typing import List


# Модель для одной пивоварни
class JSONPlaceholder(BaseModel):
    userId: int
    id: int
    title: str
    body: str

# Модель для списка
class ListJsonPlaceholder(BaseModel):
    message: List[JSONPlaceholder]

# Модель для одной записи
class SingleJsonPlaceholder(BaseModel):
    message: JSONPlaceholder