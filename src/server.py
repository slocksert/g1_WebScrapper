from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
import os
import dotenv

dotenv.load_dotenv()
host = os.getenv('MYSQL_HOST')
database = os.getenv('MYSQL_DATABASE')
password = os.getenv('MYSQL_ROOT_PASSWORD')
port = os.getenv('MYSQL_PORT')

sqlalchemy_database_url = f'mysql+pymysql://root:{password}@{host}:{port}/{database}'
engine = create_engine(sqlalchemy_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Crawler(Base):
    __tablename__ = 'crawler'
    index = Column(Integer, primary_key=True)
    news = Column(String)
    link = Column(String)
    date = Column(Date)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/news')
def list(db: Session = Depends(get_db)):
    news = db.query(Crawler).all()
    return news
