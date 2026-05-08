from sqlalchemy import Column, Integer, String, Float

from app.database.connection import Base

class Portfolio(Base):

    __tablename__ = "portfolio"

    id = Column(Integer, primary_key=True, index=True)

    user_email = Column(String)

    stock_symbol = Column(String)

    quantity = Column(Integer)

    buy_price = Column(Float)