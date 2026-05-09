from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

# Routes
from app.routes import stocks

from app.routes import user_routes

from app.routes import watchlist_routes

from app.routes import portfolio_routes

# Authentication
from app.auth import auth_routes

# WebSockets
from app.websocket import stock_ws

# -----------------------------------
# FastAPI Application
# -----------------------------------
app = FastAPI(

    title="Trading Copilot API",

    description="""
    AI Trading Copilot Backend APIs

    Features:
    - Live Stock Data
    - RSI & MACD Indicators
    - AI Trading Signals
    - News Sentiment Analysis
    - Portfolio Tracking
    - Watchlists
    - Real-Time WebSockets
    """,

    version="1.0.0",

    docs_url="/docs",

    redoc_url="/redoc"
)

# -----------------------------------
# CORS Middleware
# -----------------------------------
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# -----------------------------------
# Stock APIs
# -----------------------------------
app.include_router(

    stocks.router,

    prefix="/stocks",

    tags=["Stocks"]
)

# -----------------------------------
# Authentication APIs
# -----------------------------------
app.include_router(

    auth_routes.router,

    prefix="/auth",

    tags=["Authentication"]
)

# -----------------------------------
# User APIs
# -----------------------------------
app.include_router(

    user_routes.router,

    prefix="/user",

    tags=["User"]
)

# -----------------------------------
# Watchlist APIs
# -----------------------------------
app.include_router(

    watchlist_routes.router,

    prefix="/watchlist",

    tags=["Watchlist"]
)

# -----------------------------------
# Portfolio APIs
# -----------------------------------
app.include_router(

    portfolio_routes.router,

    prefix="/portfolio",

    tags=["Portfolio"]
)

# -----------------------------------
# WebSocket APIs
# -----------------------------------
app.include_router(

    stock_ws.router
)

# -----------------------------------
# Root Health API
# -----------------------------------
@app.get(
    "/",
    tags=["System"]
)
def home():

    return {

        "status": "success",

        "message":
        "Trading Copilot Backend Running",

        "version": "1.0.0",

        "docs":
        "/docs"
    }

# -----------------------------------
# Startup Event
# -----------------------------------
@app.on_event("startup")
async def startup_event():

    print("\n")
    print("=" * 60)

    print(
        "🚀 Trading Copilot Backend Started"
    )

    print(
        "📊 Live Market APIs Ready"
    )

    print(
        "🧠 AI Signal Engine Active"
    )

    print(
        "📰 News Sentiment System Active"
    )

    print(
        "🔌 WebSocket Streaming Ready"
    )

    print("=" * 60)
    print("\n")