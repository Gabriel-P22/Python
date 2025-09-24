from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost/school"

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()