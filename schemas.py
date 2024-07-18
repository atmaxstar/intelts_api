from pydantic import BaseModel
from typing import List

class TextBody(BaseModel):
    text: str

class TextsBody(BaseModel):
    texts: List[str]