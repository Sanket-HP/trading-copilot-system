from app.database.connection import engine, Base
from app.models.user import User
from app.models.watchlist import Watchlist
from app.models.portfolio import Portfolio
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")