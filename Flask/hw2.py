# Разработать систему регистрации пользователя, используя Pydantic для валидации входных данных,
# обработки вложенных структур и сериализации. Система должна обрабатывать данные в формате JSON.
#
# Задачи:
# 1. Создать классы моделей данных с помощью Pydantic для пользователя и его адреса.
# 2. Реализовать функцию, которая принимает JSON строку, десериализует её в объекты Pydantic,
# валидирует данные, и в случае успеха сериализует объект обратно в JSON и возвращает его.
# 3. Добавить кастомный валидатор для проверки соответствия возраста и статуса занятости пользователя.
# 4. Написать несколько примеров JSON строк для проверки различных сценариев валидации:
# успешные регистрации и случаи, когда валидация не проходит (например возраст не соответствует статусу занятости).
#
# Модели:
# Address: Должен содержать следующие поля:
# city: строка, минимум 2 символа.
# street: строка, минимум 3 символа.
# house_number: число, должно быть положительным.
#
# User: Должен содержать следующие поля:
# name: строка, должна быть только из букв, минимум 2 символа.
# age: число, должно быть между 0 и 120.
# email: строка, должна соответствовать формату email.
# is_employed: булево значение, статус занятости пользователя.
# address: вложенная модель адреса.
#
# Валидация:
# Проверка, что если пользователь указывает, что он занят (is_employed = true), его возраст должен быть от 18 до 65 лет.


from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError
from pydantic_core.core_schema import ValidationInfo


class Address(BaseModel):
    city: str = Field(
        min_length=2
    )
    street: str = Field(
        min_length=3
    )
    house_number: int = Field(
        gt=0
    )


class User(BaseModel):
    name: str = Field(
        min_length=2
    )
    age: int = Field(
        gt=0,
        lt=120
    )
    email: EmailStr
    is_employed: bool
    address: Address



@field_validator('is_employed')
@classmethod
def check_is_employed(cls, value: bool, values: ValidationInfo):
    age = values.data.get('age')
    if value and (age < 18 or age >= 65):
        raise ValueError("Возраст рабочего должен быть в диапазоне от 18 до 65 лет.")
    return value


def check_json(data_json):
    try:
        user = User.model_validate_json(data_json)
        print("Все переданные данные валидны")
        return user.model_dump_json(indent=4)
    except ValidationError as e:
        return f'Ошибка при валидации: {e}'


json_input = """{
    "name": "John Doe",
    "age": 70,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""


try:
    user = check_json(json_input)
    print(user)
except ValidationError as e:
    print(f'Ошибка при валидации: {e}')