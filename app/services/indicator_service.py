import yfinance as yf
import pandas as pd
import ta

# RSI Indicator
def calculate_rsi(symbol: str):

    stock = yf.Ticker(symbol)

    df = stock.history(period="3mo")

    df["RSI"] = ta.momentum.RSIIndicator(
        close=df["Close"]
    ).rsi()

    latest_rsi = df["RSI"].iloc[-1]

    signal = "NEUTRAL"

    if latest_rsi < 30:
        signal = "BUY"

    elif latest_rsi > 70:
        signal = "SELL"

    return {
        "symbol": symbol,
        "RSI": round(float(latest_rsi), 2),
        "signal": signal
    }

# MACD Indicator
def calculate_macd(symbol: str):

    stock = yf.Ticker(symbol)

    df = stock.history(period="3mo")

    macd = ta.trend.MACD(close=df["Close"])

    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()

    latest_macd = df["MACD"].iloc[-1]
    latest_signal = df["MACD_SIGNAL"].iloc[-1]

    trend = "BEARISH"

    if latest_macd > latest_signal:
        trend = "BULLISH"

    return {
        "symbol": symbol,
        "macd": round(float(latest_macd), 2),
        "signal_line": round(float(latest_signal), 2),
        "trend": trend
    }

    # AI Signal Engine
# Advanced AI Signal Engine
def generate_ai_signal(symbol: str):

    rsi_data = calculate_rsi(symbol)

    macd_data = calculate_macd(symbol)

    rsi_value = rsi_data["RSI"]

    macd_trend = macd_data["trend"]

    score = 0

    reasons = []

    # RSI Analysis
    if rsi_value < 30:

        score += 40

        reasons.append(
            "RSI shows oversold condition"
        )

    elif rsi_value > 70:

        score -= 40

        reasons.append(
            "RSI shows overbought condition"
        )

    else:

        reasons.append(
            "RSI is neutral"
        )

    # MACD Analysis
    if macd_trend == "BULLISH":

        score += 30

        reasons.append(
            "MACD indicates bullish momentum"
        )

    else:

        score -= 30

        reasons.append(
            "MACD indicates bearish momentum"
        )

    # AI Decision
    signal = "HOLD"

    confidence = abs(score)

    if score >= 50:

        signal = "BUY"

    elif score <= -50:

        signal = "SELL"

    else:

        signal = "HOLD"

    return {
        "symbol": symbol,
        "AI_SIGNAL": signal,
        "confidence": confidence,
        "score": score,
        "RSI": round(rsi_value, 2),
        "MACD_TREND": macd_trend,
        "analysis": reasons
    }