import yfinance as yf

# Get Live Stock Price
def get_live_stock_price(symbol: str):

    stock = yf.Ticker(symbol)

    data = stock.history(period="1d")

    latest_price = data["Close"].iloc[-1]

    return {
        "symbol": symbol,
        "live_price": round(float(latest_price), 2)
    }

# Get Historical Data
def get_stock_history(symbol: str):

    stock = yf.Ticker(symbol)

    history = stock.history(period="5d")

    result = []

    for index, row in history.iterrows():

        result.append({
            "date": str(index.date()),
            "open": round(float(row["Open"]), 2),
            "high": round(float(row["High"]), 2),
            "low": round(float(row["Low"]), 2),
            "close": round(float(row["Close"]), 2),
            "volume": int(row["Volume"])
        })

    return result