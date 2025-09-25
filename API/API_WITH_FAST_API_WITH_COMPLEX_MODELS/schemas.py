from typing import List, Optional
from pydantic import BaseModel

class Profile(BaseModel):
    id: int
    age: int
    address: str

    class Config:
        from_attributes = True

class ProfileCreate(BaseModel):
    age: int
    address: str

class Student(BaseModel):
    id: int
    name: str
    profile: Optional[Profile] = None

    class Config:
        from_attributes = True

class StudentCreate(BaseModel):
    name: str
    email: str
    profile: ProfileCreate

