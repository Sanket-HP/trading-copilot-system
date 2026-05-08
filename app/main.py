from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import stocks
from app.routes import user_routes
from app.routes import watchlist_routes
from app.routes import portfolio_routes

from app.auth import auth_routes

from app.websocket import stock_ws

app = FastAPI(
    title="Trading Copilot API",
    description="AI Trading Copilot Backend APIs",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Stock Routes
app.include_router(
    stocks.router,
    prefix="/stocks",
    tags=["Stocks"]
)

# Authentication Routes
app.include_router(
    auth_routes.router,
    prefix="/auth",
    tags=["Authentication"]
)

# User Routes
app.include_router(
    user_routes.router,
    prefix="/user",
    tags=["User"]
)

# Watchlist Routes
app.include_router(
    watchlist_routes.router,
    prefix="/watchlist",
    tags=["Watchlist"]
)

# Portfolio Routes
app.include_router(
    portfolio_routes.router,
    prefix="/portfolio",
    tags=["Portfolio"]
)

# WebSocket Routes
app.include_router(stock_ws.router)

# Home Route
@app.get("/")
def home():

    return {
        "status": "success",
        "message": "Trading Copilot Backend Running Successfully"
    }