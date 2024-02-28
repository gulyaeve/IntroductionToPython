import datetime
import json
from typing import Optional

from pydantic import BaseModel, EmailStr, constr, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber


class RussiaPhone(PhoneNumber):
    supported_regions = ["RU"]
    default_region_code = "+7"
    # max_length = 12
    # min_length = 12


class User(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    date_birth: datetime.date
    phone: Optional[RussiaPhone] = None

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Вам должно быть более 18 лет")
        return value

    @field_validator("phone", mode="before")
    def validate_phone(cls, value: str):
        if value:
            if value.startswith("8"):
                value = value.replace("8", "+7", 1)
        return value


user1: User = User(
    id=1,
    name="Vasya",
    age=18,
    date_birth=datetime.date(1988, 10, 30),
    email="vasya@mail.ru",
    password="12345678",
    phone="+79321234567"
)

user2_json = json.loads("""{
"id": 2,
"name": "Petya",
"age": 25,
"email": "petya@mail.ru",
"password": "87654321",
"date_birth": "1990-10-30",
"phone": null
}""")

user2 = User(**user2_json)

if __name__ == '__main__':
    print(repr(user1))
    print(user1.phone)

    print(user1.model_dump())
    print(user1.model_dump_json(indent=4))
    print(user2)
