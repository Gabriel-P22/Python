from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
import models, schemas
from database import engine, sessionLocal
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/students/', response_model=schemas.Student)
def create_student(
        student: schemas.StudentCreate,
        db: Session = Depends(get_db)
):
    db_student = models.Student(
        name = student.name,
        profile = models.Profile(**student.profile.model_dump())
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/students/', response_model=List[schemas.Student])
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).options(
        joinedload(models.Student.profile)
    ).all()

    return students