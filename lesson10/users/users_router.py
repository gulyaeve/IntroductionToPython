from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from lesson10.users.schemas import User, user1, user2


class ProjectException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)


class UserNotFound(ProjectException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Пользователь не найден"


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.get("")
async def get_users() -> list[User]:
    users = [user1, user2]
    return users


@router.get("/{user_id}")
async def get_user(user_id: int) -> User:
    match user_id:
        case 1:
            return user1
        case 2:
            return user2
        case _:
            raise UserNotFound


@router.post("")
async def register_user(user: User) -> User:
    return user
