from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    name: str
    last_name: str
    age: int
    skills : List[str] = []