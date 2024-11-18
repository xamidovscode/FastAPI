from fastapi import APIRouter, HTTPException  # Модуль для создания роутеров
from models.user import User  # Импорт модели пользователя

# Создаем роутер
router = APIRouter()

# Эндпоинт для создания пользователя
@router.post("/users/")
async def create_user(username: str, email: str, password: str):
    hashed_password = f"hashed-{password}"  # Здесь должна быть логика хэширования
    user = await User.create(
        username=username,
        email=email,
        hashed_password=hashed_password,
    )
    return {"id": user.id, "username": user.username, "email": user.email}

# Эндпоинт для получения пользователя по ID
@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await User.filter(id=user_id).first()  # Поиск пользователя по ID
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"id": user.id, "username": user.username, "email": user.email}
