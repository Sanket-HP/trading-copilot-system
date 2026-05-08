from fastapi import APIRouter

from app.services.market_service import (
    get_live_stock_price,
    get_stock_history
)

from app.services.indicator_service import (
    calculate_rsi,
    calculate_macd,
    generate_ai_signal
)

router = APIRouter()

# Live Stock API
@router.get("/live/{symbol}")
def live_stock(symbol: str):

    return get_live_stock_price(symbol)

# Historical Data API
@router.get("/history/{symbol}")
def history(symbol: str):

    return get_stock_history(symbol)

# RSI API
@router.get("/rsi/{symbol}")
def rsi(symbol: str):

    return calculate_rsi(symbol)

# MACD API
@router.get("/macd/{symbol}")
def macd(symbol: str):

    return calculate_macd(symbol)

# Trending Stocks
@router.get("/trending")
def trending_stocks():

    return {
        "stocks": [
            "RELIANCE.NS",
            "TCS.NS",
            "INFY.NS",
            "HDFCBANK.NS"
        ]
    }

    # AI Signal API
@router.get("/ai-signal/{symbol}")
def ai_signal(symbol: str):

    return generate_ai_signal(symbol)