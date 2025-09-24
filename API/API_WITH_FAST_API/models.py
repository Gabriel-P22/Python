from sqlalchemy import \
    Column, Integer, String, ForeignKey

from database import Base

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

class Registrations(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(100), nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'))

