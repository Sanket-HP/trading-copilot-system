from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import User

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"

security = HTTPBearer()

# Verify JWT Token
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid authentication credentials"
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise credentials_exception

    return user