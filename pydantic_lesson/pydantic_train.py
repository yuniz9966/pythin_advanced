# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     is_active: bool
#
#
# user = User(
#     id=1,
#     name="Dima",
#     age=23,
#     is_active=True
# )
#
# print(user)

# print(User.name)
#
#
# my_var: int
#
# print(my_var)

# ==================================================================================

# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     first_name: str
#     last_name: str
#     age: int
#
#
# class Admin(User):
#     salary_rating: float
#
#
# class Moderator(User):
#     phone: str
#
#
# user = User(
#     first_name='Vlad',
#     last_name="Black",
#     age=23
# )
#
# print(user)
#
# admin = Admin(
#     first_name='Jessika',
#     last_name="Black",
#     age=27,
#     salary_rating=2.4,
# )
# print(admin)
#
# moder = Moderator(
#     first_name='Mila',
#     last_name="Green",
#     age=31,
#     phone='+1234567890',
# )
# print(moder)

# ==================================================================================

from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str = Field(
        min_length=4,
        max_length=15,
        description="Name of user"
    )
    last_name: str = Field(
        default="Black",
        min_length=2,
        max_length=30,
    )
    age: int = Field(
        gt=0,
        lt=100
    )


user = User(
    first_name='John',
    age=19
)

print(user)

# ==================================================================================

from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError


class User(BaseModel):
    name: str = Field(
        min_length=4,
        max_length=15
    )
    age: int = Field(
        gt=0,
        lt=100
    )
    email: EmailStr

    @field_validator('email')
    @classmethod
    def check_email_domain(cls, value: str) -> str: # value="test.email@gmail.com"
        allowed_domains = {"gmail.com",}
        raw_domain = value.split('@')[-1]

        if raw_domain not in allowed_domains:
            raise ValueError(f"Email must be from one of the following domains: {', '.join(allowed_domains)}")

        return value

json_data = [
    """{"name": "Andre","age": 21,"email": "a.21@gmail.com"}""",
    """{"name": "Andre","age": 22,"email": "a.22@gmail.com"}""",
    """{"name": "Andre","age": 23,"email": "a.23@gmail.com"}""",
    """{"name": "Andre","age": 24,"email": "a.24@test.com"}""",
    """{"name": "Andre","age": 25,"email": "a.25@gmail.com"}""",
    """{"name": "Andre","age": 25,"email": "a.25@test.com"}"""
]

for us in json_data:
    try:
        user = User.model_validate_json(us)
        print(user)
    except ValidationError as err:
        print(err)



print("WE ARE IN THE SYSTEM!!!")