from dataclasses import dataclass
from typing import Sequence
from module_enum import Manufacturers


@dataclass
class Car:
    id: int
    manufacturer: Manufacturers
    model: str
    engine: str


@dataclass
class User:
    id: int
    name: str
    email: str
    site: str | None = None
    cars: list[Car] | None = None

    def __str__(self):
        # return f"Name: {self.name}"
        return repr(self)

    # def __add__(self, car: Car):
    #     self.cars.append(car)


class Users:
    def __init__(self, users: Sequence[User]):
        self._users = users
        # self._users = list(users)

    def __getitem__(self, key: int) -> User:
        return self._users[key]

    def __repr__(self):
        _out = []
        for _user in self._users:
            _out.append(_user)
        return str(_out)

    def __add__(self, new_user: User):
        if isinstance(self._users, list):
            self._users.append(new_user)
            return self._users
        else:
            raise TypeError
        # return Users(self._users + new_user)


car_1 = Car(1, Manufacturers.BMW.value, "m3", "v8")
user_1 = User(
    id=1,
    name="Vasya",
    email="vasya@ya.ru",
    cars=[
        car_1,
        Car(2, "Lada", "7", "v12"),
    ]
)

# print(user_1)

# user_1 += Car(3, "Volga", "24", "v8")
# print(user_1)

users = Users((
    user_1,
    User(2, "Petya", "petya@ya.ru")
))

for u in users:
    print(u)

print(users[0])

print(users)

str_user = "User(id=3, name='Masha', email='masha@ya.ru', site=None, cars=None)"
user_3 = eval(str_user)
print(type(user_3))

# users += user_3
print(users)

car_3 = Car(4, Manufacturers.GAZ)

