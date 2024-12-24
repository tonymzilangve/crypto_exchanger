from pydantic import BaseModel


class Currency(BaseModel):
    name: str
    code: int    
