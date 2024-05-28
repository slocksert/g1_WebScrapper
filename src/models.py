from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from src.database import engine

from src.config import database

Base = declarative_base()

class G1Scrapper(Base):
    __tablename__ = f'{database}'
    index = Column(Integer(), primary_key=True, autoincrement=True)
    news = Column(String(355), unique=True)
    link = Column(String(355), unique=True)
    date = Column(Date())
    image = Column(String(355), unique=True)

Base.metadata.create_all(bind=engine)