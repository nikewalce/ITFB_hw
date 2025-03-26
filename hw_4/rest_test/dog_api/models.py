from pydantic import BaseModel, HttpUrl
from typing import List, Dict


# Модели Pydantic
class BreedListResponse(BaseModel):
    message: Dict[str, List[str]]
    status: str


class RandomImageResponse(BaseModel):
    message: HttpUrl
    status: str


class MultipleImagesResponse(BaseModel):
    message: List[HttpUrl]
    status: str


class BreedSubListResponse(BaseModel):
    message: List[str]
    status: str