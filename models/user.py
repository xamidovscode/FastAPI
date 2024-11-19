from tortoise.models import Model  # Основной класс для создания моделей
from tortoise import fields  # Поля для моделей

# Определение модели пользователя
class User(Model):
    id = fields.IntField(pk=True)  # Первичный ключ
    username = fields.CharField(max_length=150, unique=False)  # Уникальное имя пользователя
    email = fields.CharField(max_length=255, unique=True)  # Уникальный email
    hashed_password = fields.CharField(max_length=255)  # Хэшированный пароль
    is_active = fields.BooleanField(default=True)  # Флаг активности пользователя

    class Meta:
        table = "users"  # Название таблицы в базе данных
