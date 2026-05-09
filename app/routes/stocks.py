from fastapi import APIRouter

# Market Services
from app.services.market_service import (

    get_live_stock_price,

    get_stock_history
)

# Technical Indicators
from app.services.indicator_service import (

    calculate_rsi,

    calculate_macd,

    generate_ai_signal
)

# News Sentiment
from app.services.news_service import (

    get_news_sentiment
)

router = APIRouter()

# -----------------------------------
# Health Check
# -----------------------------------
@router.get("/")
def stock_home():

    return {

        "status": "success",

        "message":
        "Stock APIs Running Successfully"
    }

# -----------------------------------
# Live Stock API
# -----------------------------------
@router.get("/live/{symbol}")
def live_stock(symbol: str):

    return get_live_stock_price(symbol)

# -----------------------------------
# Historical Data API
# -----------------------------------
@router.get("/history/{symbol}")
def history(symbol: str):

    return get_stock_history(symbol)

# -----------------------------------
# RSI Indicator API
# -----------------------------------
@router.get("/rsi/{symbol}")
def rsi(symbol: str):

    return calculate_rsi(symbol)

# -----------------------------------
# MACD Indicator API
# -----------------------------------
@router.get("/macd/{symbol}")
def macd(symbol: str):

    return calculate_macd(symbol)

# -----------------------------------
# AI Signal API
# -----------------------------------
@router.get("/ai-signal/{symbol}")
def ai_signal(symbol: str):

    return generate_ai_signal(symbol)

# -----------------------------------
# AI News Sentiment API
# -----------------------------------
@router.get("/news-sentiment/{symbol}")
def news_sentiment(symbol: str):

    return get_news_sentiment(symbol)

# -----------------------------------
# Trending Stocks API
# -----------------------------------
@router.get("/trending")
def trending_stocks():

    return {

        "market": "NSE",

        "stocks": [

            {
                "symbol": "RELIANCE.NS",
                "name": "Reliance Industries"
            },

            {
                "symbol": "TCS.NS",
                "name": "Tata Consultancy Services"
            },

            {
                "symbol": "INFY.NS",
                "name": "Infosys"
            },

            {
                "symbol": "HDFCBANK.NS",
                "name": "HDFC Bank"
            }
        ]
    }