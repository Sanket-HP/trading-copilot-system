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
# Health Check API
# -----------------------------------
@router.get("/")
def stock_home():

    return {

        "status": "success",

        "message":
        "Trading Copilot APIs Running"
    }

# -----------------------------------
# Live Stock API
# -----------------------------------
@router.get("/live/{symbol}")
def live_stock(symbol: str):

    return get_live_stock_price(symbol)

# -----------------------------------
# Historical Stock Data API
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
                "name":
                "Reliance Industries"
            },

            {
                "symbol": "TCS.NS",
                "name":
                "Tata Consultancy Services"
            },

            {
                "symbol": "INFY.NS",
                "name":
                "Infosys"
            },

            {
                "symbol": "HDFCBANK.NS",
                "name":
                "HDFC Bank"
            }
        ]
    }

# -----------------------------------
# Multi Stock Market Overview API
# -----------------------------------
@router.get("/market-overview")
def market_overview():

    stocks = [

        "RELIANCE.NS",

        "TCS.NS",

        "INFY.NS",

        "HDFCBANK.NS"
    ]

    results = []

    for symbol in stocks:

        try:

            # Live Price
            live = get_live_stock_price(
                symbol
            )

            # RSI
            rsi_data = calculate_rsi(
                symbol
            )

            # MACD
            macd_data = calculate_macd(
                symbol
            )

            # AI Signal
            ai_data = generate_ai_signal(
                symbol
            )

            # News Sentiment
            news_data = get_news_sentiment(
                symbol
            )

            results.append({

                "symbol": symbol,

                "price":
                live["live_price"],

                "RSI":
                rsi_data["RSI"],

                "MACD":
                macd_data["macd"],

                "trend":
                macd_data["trend"],

                "signal":
                ai_data["AI_SIGNAL"],

                "confidence":
                ai_data["confidence"],

                "news_sentiment":
                news_data["sentiment"]
            })

        except Exception as e:

            results.append({

                "symbol": symbol,

                "error": str(e)
            })

    return {

        "market": results
    }