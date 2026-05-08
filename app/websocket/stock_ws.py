from fastapi import APIRouter, WebSocket
import asyncio
import yfinance as yf

router = APIRouter()

# Live WebSocket Stock Stream
@router.websocket("/ws/stocks/{symbol}")
async def websocket_stock_data(
    websocket: WebSocket,
    symbol: str
):

    await websocket.accept()

    while True:

        try:

            stock = yf.Ticker(symbol)

            data = stock.history(period="1d")

            live_price = round(
                float(data["Close"].iloc[-1]),
                2
            )

            await websocket.send_json({
                "symbol": symbol,
                "live_price": live_price
            })

            await asyncio.sleep(5)

        except Exception as e:

            await websocket.send_json({
                "error": str(e)
            })

            break