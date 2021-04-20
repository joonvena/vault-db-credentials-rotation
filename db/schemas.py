from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True
