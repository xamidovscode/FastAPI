from pydantic import BaseModel, EmailStr, Field  # Импорт Pydantic моделей


class UserCreate(BaseModel):
    username: str   # Поле username с ограничением длины
    email: EmailStr  # Email с автоматической валидацией
    password: str

    class Config:
        orm_mode = True



class UsersList(BaseModel):
    id: int
    username: str   # Поле username с ограничением длины
    email: EmailStr  # Email с автоматической валидацией
    hashed_password: str

    class Config:
        orm_mode = True