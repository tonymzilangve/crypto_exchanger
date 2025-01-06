from pydantic import BaseModel, Field


class Currency(BaseModel):
    name: str
    code: str = Field(min_length=3, max_length=3)
