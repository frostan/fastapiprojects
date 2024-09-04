from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class SecondUser(BaseModel):
    name: str
    age: int


class FeedBack(BaseModel):
    name: str
    message: str
