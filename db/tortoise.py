from tortoise import Tortoise  # Основной модуль Tortoise ORM
from config import DATABASE_URL  # Импорт строки подключения

modules = {'models': ["models.user"]}

# Path to your Tortoise configuration
TORTOISE_ORM = {
    "connections": {
        "default": "postgres://fastapi:fastapi@localhost:5432/fastapi",  # Replace with your DB connection string
    },
    "apps": {
        "models": {
            "models": modules.get("models", []) + ["aerich.models"],  # Include aerich models
            "default_connection": "default",
        },
    },
}

# Функция для инициализации базы данных
async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,  # Подключение к базе данных
        modules={"models": ["models.user"]},  # Указание путей к моделям
    )
    await Tortoise.generate_schemas()  # Генерация схем

# Функция для завершения соединения с базой данных
async def close_db():
    await Tortoise.close_connections()
