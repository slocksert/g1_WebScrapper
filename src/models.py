from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from database import engine

from config import database

Base = declarative_base()

class Crawler(Base):
    __tablename__ = f'{database}'
    index = Column(Integer, primary_key=True)
    news = Column(String(150))
    link = Column(String(150))
    date = Column(Date())

Base.metadata.create_all(bind=engine)