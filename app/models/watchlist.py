from sqlalchemy import Column, Integer, String

from app.database.connection import Base

class Watchlist(Base):

    __tablename__ = "watchlist"

    id = Column(Integer, primary_key=True, index=True)

    user_email = Column(String)

    stock_symbol = Column(String)