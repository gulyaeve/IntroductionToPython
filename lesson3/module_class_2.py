

class Database:
    @classmethod
    def make_connect(cls, srv: str, port: int):
        print(f"Connected {srv}, {port}")

    @staticmethod
    def some_func(a):
        return a * 2


Database.make_connect(srv="Yandex.ru", port=22)

x = Database()
x.some_func(2)
