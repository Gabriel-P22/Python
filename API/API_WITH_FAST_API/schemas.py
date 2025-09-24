from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        from_attributes = True

class RegistrationsBase(BaseModel):
    student_id: int
    subject: str

class RegistrationsCreate(RegistrationsBase):
    pass

class RegistrationsResponse(RegistrationsBase):
    id: int
    class Config:
        from_attributes = True
