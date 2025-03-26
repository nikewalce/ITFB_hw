from pydantic import BaseModel

class URLStatusModel(BaseModel):
    url: str
    status_code: int

    @classmethod
    def validate(cls, url: str, status_code: int):
        return cls(url=url, status_code=status_code)
