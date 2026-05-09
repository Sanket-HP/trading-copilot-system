import feedparser

from vaderSentiment.vaderSentiment import (
    SentimentIntensityAnalyzer
)

# Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Company Name Mapping
COMPANY_NAMES = {

    "RELIANCE.NS":
    "Reliance Industries",

    "TCS.NS":
    "Tata Consultancy Services",

    "INFY.NS":
    "Infosys",

    "HDFCBANK.NS":
    "HDFC Bank"
}

# News Sentiment Function
def get_news_sentiment(symbol: str):

    # Company Name
    company = COMPANY_NAMES.get(
        symbol,
        symbol
    )

    # Search Query
    query = company.replace(
        " ",
        "+"
    )

    # Google News RSS
    url = (
         f"https://news.google.com/rss/search?q={query}+stock+market"
    )

    # Parse News Feed
    feed = feedparser.parse(url)

    # No News Found
    if not feed.entries:

        return {

            "symbol": symbol,

            "headline":
            "No recent financial news found.",

            "sentiment": "NEUTRAL",

            "confidence": 0
        }

    # First Article
    article = feed.entries[0]

    headline = article.title

    # Sentiment Score
    score = analyzer.polarity_scores(
        headline
    )["compound"]

    # Default Sentiment
    sentiment = "NEUTRAL"

    # Bullish
    if score > 0.2:

        sentiment = "BULLISH"

    # Bearish
    elif score < -0.2:

        sentiment = "BEARISH"

    # Confidence Score
    confidence = round(
        abs(score) * 100,
        2
    )

    return {

        "symbol": symbol,

        "headline": headline,

        "sentiment": sentiment,

        "confidence": confidence
    }