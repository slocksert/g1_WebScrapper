from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import password, port, database

sqlalchemy_database_url = f'mysql+pymysql://root:{password}@127.0.0.1:{port}/{database}'
engine = create_engine(sqlalchemy_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()