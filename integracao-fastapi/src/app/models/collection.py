from pydantic import BaseModel
from typing import List
from .image import Image

class Collection(BaseModel):
    id: int
    name: str
    images: List[Image] = []
