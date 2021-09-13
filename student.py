from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    id: str
    name: str
    last_name: str
    age: int
    skills : List[str] = []