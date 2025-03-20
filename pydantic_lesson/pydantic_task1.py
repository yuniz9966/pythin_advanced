from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    city: str
    street: str
    house_number: int

class User(BaseModel):
    name:str
    age:int
    email: EmailStr
    address:Address

user_data = """
{
    "name": "Vlad",
    "age": "2_128",
    "email": "john.doee@xample.a",
    "address": {
        "city": "New York",
        "street": "St. Time Square",
        "house_number": 2
    }
}
"""

user = User.model_validate_json(user_data)

print(user)