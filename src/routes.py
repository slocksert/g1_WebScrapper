from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from models import Crawler
from database import get_db

crawler = APIRouter()

@crawler.get('/news')
def list(db: Session = Depends(get_db)):
    news = db.query(Crawler).all()
    return news