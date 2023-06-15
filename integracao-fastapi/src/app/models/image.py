from fastapi import UploadFile, File
from pydantic import BaseModel

class Image(BaseModel):
    id: int
    url: str = None
    content: UploadFile = File(...)
    collection_id: int = None
