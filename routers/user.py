from fastapi import APIRouter, HTTPException

from models.user import User
from schemas.user import UserCreate, UsersList

# Создаем роутер
router = APIRouter()


@router.post("/user/create/")
async def create_user(user_data: UserCreate):
    # Проверяем, существует ли пользователь с таким email
    existing_user = await User.filter(email=user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким email уже существует",
        )

    # Хэшируем пароль (пример, лучше использовать библиотеку bcrypt)
    hashed_password = f"hashed-{user_data.password}"

    # Создаем пользователя
    user = await User.create(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password,
    )
    return user


@router.get(
    "/user/list",
    response_model=list[UsersList]
)
async def get_all_users():
    return await User.all()