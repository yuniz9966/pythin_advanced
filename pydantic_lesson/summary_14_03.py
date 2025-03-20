from pydantic import BaseModel, Field, model_validator, ValidationError, EmailStr
from typing import Union


class User(BaseModel):
    user_name: str = Field(min_length=4)
    email: EmailStr
    password: str = Field(min_length=9)


    @model_validator(mode='before')
    @classmethod
    def check_raw_data(cls, data: dict[str, str]) -> dict[str, str]:
        repeat_password = data.pop('repeat_password')
        password = data.get('password')

        if password != repeat_password:
            raise ValueError("Пароли должны совпадать")

        return data



json_data = [
    """{"user_name": "Vlad", "email": "test.email@gmail.com", "password": "as8df7gtsd87fg5sd76fg", "repeat_password": "as8df7gtsd8776fg"}"""
]


for obj in json_data:
    try:
        user = User.model_validate_json(obj)
        print(user)
    except ValidationError as err:
        print(err)

# =========================================================================================

from pydantic import BaseModel, Field, AliasChoices


class Item(BaseModel):
    in_stock: bool = Field(
        validation_alias=AliasChoices(
            'in_stock',
            'available',
            'Is available',
            'In Stock',
            'is-available'
        )
    )
    price: float


# json_data = '{"name": "Laptop", "available": true}'
# json_data = '{"name": "Laptop", "in_stock": true}'

json_data = [
    """{"in_stock": true, "price": 1.1}""",
    """{"available": false, "price": 1.2}""",
    """{"Is available": false, "price": 13.3}""",
    """{"In Stock": false, "price": 14.22}""",
    """{"is-available": false, "price": 14.22}"""
]


for obj in json_data:
    try:
        item = Item.model_validate_json(obj)
        print(item)
    except ValidationError as err:
        print(err)


# ========================================================================================
# Field aliases
# ========================================================================================

from pydantic import BaseModel, Field, AliasChoices


class Event(BaseModel):
    title: str

    class Config:
       validate_assignment = True
       str_strip_whitespace = True
       str_min_length = 5


event = Event(title="     Summary 1       ")

print(event)
event.title = 'Hi'
print(event)