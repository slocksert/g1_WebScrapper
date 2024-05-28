from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import password, port, database, host

DBURL = f'mysql+pymysql://root:{password}@{host}:{port}/{database}'
engine = create_engine(DBURL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()