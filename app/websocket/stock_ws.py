from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect

import asyncio
import yfinance as yf

from datetime import datetime

router = APIRouter()

# Live WebSocket Stock Stream
@router.websocket("/ws/stocks/{symbol}")
async def websocket_stock_data(
    websocket: WebSocket,
    symbol: str
):

    await websocket.accept()

    print(f"WebSocket connected: {symbol}")

    try:

        while True:

            try:

                # Fetch Stock Data
                stock = yf.Ticker(symbol)

                data = stock.history(
                    period="1d"
                )

                # No Data
                if data.empty:

                    await websocket.send_json({

                        "status": "error",

                        "message":
                        f"No market data found for {symbol}"
                    })

                    await asyncio.sleep(5)

                    continue

                latest = data.iloc[-1]

                # Prices
                open_price = round(
                    float(latest["Open"]),
                    2
                )

                close_price = round(
                    float(latest["Close"]),
                    2
                )

                high_price = round(
                    float(latest["High"]),
                    2
                )

                low_price = round(
                    float(latest["Low"]),
                    2
                )

                # Volume
                volume = int(
                    latest["Volume"]
                )

                # Price Change
                change = round(
                    close_price - open_price,
                    2
                )

                # Percentage Change
                change_percent = 0

                if open_price != 0:

                    change_percent = round(

                        (change / open_price) * 100,
                        2
                    )

                # Trend
                trend = "NEUTRAL"

                if change > 0:

                    trend = "BULLISH"

                elif change < 0:

                    trend = "BEARISH"

                # Direction
                direction = "SIDEWAYS"

                if change > 0:

                    direction = "UP"

                elif change < 0:

                    direction = "DOWN"

                # Volatility
                volatility = round(
                    ((high_price - low_price)
                    / open_price) * 100,
                    2
                )

                # Volatility Level
                volatility_level = "LOW"

                if volatility > 2:

                    volatility_level = "MEDIUM"

                if volatility > 5:

                    volatility_level = "HIGH"

                # Trading Score
                trade_score = 50

                if trend == "BULLISH":

                    trade_score += 20

                if volatility < 2:

                    trade_score += 10

                if volume > 1000000:

                    trade_score += 10

                if change_percent > 2:

                    trade_score += 10

                # Market Status
                market_status = "OPEN"

                now = datetime.now()

                current_hour = now.hour

                current_minute = now.minute

                if (
                    current_hour < 9
                    or
                    (current_hour == 9 and current_minute < 15)
                    or
                    current_hour >= 15
                ):

                    market_status = "CLOSED"

                # Timestamp
                timestamp = now.strftime(
                    "%H:%M:%S"
                )

                # Send Live Data
                await websocket.send_json({

                    "status": "success",

                    "symbol": symbol,

                    "live_price": close_price,

                    "open": open_price,

                    "high": high_price,

                    "low": low_price,

                    "change": change,

                    "change_percent": change_percent,

                    "trend": trend,

                    "direction": direction,

                    "market_status": market_status,

                    "volume": volume,

                    "volatility": volatility,

                    "volatility_level":
                    volatility_level,

                    "trade_score": trade_score,

                    "timestamp": timestamp
                })

            except Exception as inner_error:

                print(
                    f"Market Fetch Error: {inner_error}"
                )

                await websocket.send_json({

                    "status": "error",

                    "message": str(inner_error)
                })

            # Refresh Every 5 Seconds
            await asyncio.sleep(5)

    except WebSocketDisconnect:

        print(
            f"WebSocket disconnected: {symbol}"
        )

    except Exception as e:

        print(
            f"WebSocket error: {e}"
        )