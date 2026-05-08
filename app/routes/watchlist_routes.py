from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.watchlist import Watchlist
from app.models.user import User

from app.auth.auth_bearer import get_current_user

router = APIRouter()

# Add Stock to Watchlist
@router.post("/add/{symbol}")
def add_watchlist(
    symbol: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    stock = Watchlist(
        user_email=current_user.email,
        stock_symbol=symbol
    )

    db.add(stock)

    db.commit()

    return {
        "message": f"{symbol} added to watchlist"
    }

# Get Watchlist
@router.get("/")
def get_watchlist(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    stocks = db.query(Watchlist).filter(
        Watchlist.user_email == current_user.email
    ).all()

    return stocks