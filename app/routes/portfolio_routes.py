from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.portfolio import Portfolio
from app.models.user import User

from app.auth.auth_bearer import get_current_user

from app.services.market_service import get_live_stock_price

router = APIRouter()

# Buy Stock
@router.post("/buy/{symbol}")
def buy_stock(
    symbol: str,
    quantity: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    live_data = get_live_stock_price(symbol)

    stock = Portfolio(
        user_email=current_user.email,
        stock_symbol=symbol,
        quantity=quantity,
        buy_price=live_data["live_price"]
    )

    db.add(stock)

    db.commit()

    return {
        "message": f"{quantity} shares of {symbol} purchased",
        "buy_price": live_data["live_price"]
    }

# View Portfolio
@router.get("/")
def get_portfolio(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    portfolio = db.query(Portfolio).filter(
        Portfolio.user_email == current_user.email
    ).all()

    result = []

    total_value = 0

    for stock in portfolio:

        live_data = get_live_stock_price(
            stock.stock_symbol
        )

        current_price = live_data["live_price"]

        investment = stock.buy_price * stock.quantity

        current_value = current_price * stock.quantity

        profit_loss = current_value - investment

        total_value += current_value

        result.append({
            "symbol": stock.stock_symbol,
            "quantity": stock.quantity,
            "buy_price": stock.buy_price,
            "current_price": current_price,
            "profit_loss": round(profit_loss, 2)
        })

    return {
        "portfolio": result,
        "total_portfolio_value": round(total_value, 2)
    }