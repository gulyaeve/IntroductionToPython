import os


if __name__ == '__main__':
    name = os.environ.get("USERNAME")
    print(name)

    postgres_user = os.environ.get("POSTGRES_USER")
    print(postgres_user)
