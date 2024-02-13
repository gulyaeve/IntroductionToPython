

class Database:
    @classmethod
    def make_connect(cls, srv: str, port: int):
        print(f"Connected {srv}, {port}")


Database.make_connect(srv="Yandex.ru", port=22)
