from fastapi import APIRouter, Depends

from app.auth.auth_bearer import get_current_user
from app.models.user import User

router = APIRouter()

# Protected User Profile API
@router.get("/profile")
def get_profile(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }