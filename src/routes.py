from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.models import G1Scrapper
from src.database import get_db

g1scrapper = APIRouter()

@g1scrapper.get('/news')
def list(db: Session = Depends(get_db)):
    news = db.query(G1Scrapper).all()
    return news