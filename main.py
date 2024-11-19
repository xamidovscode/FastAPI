from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise  # Подключение Tortoise ORM

from db.tortoise import modules
from routers import user  # Импорт роутеров

# Создаем приложение FastAPI
app = FastAPI()

# Подключаем роутеры
app.include_router(user.router)

# Настройка Tortoise ORM
register_tortoise(
    app,
    db_url="postgres://fastapi:fastapi@localhost:5432/fastapi",  # URL для подключения к базе данных PostgreSQL
    modules=modules,  # Путь к вашим моделям
    generate_schemas=True,  # Автоматическое создание схем в базе данных
    add_exception_handlers=True,  # Добавление обработчиков ошибок для базы данных
)

# Тестовый эндпоинт
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в проект FastAPI с Tortoise ORM"}
