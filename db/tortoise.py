from tortoise import Tortoise  # Основной модуль Tortoise ORM
from config import DATABASE_URL  # Импорт строки подключения

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
