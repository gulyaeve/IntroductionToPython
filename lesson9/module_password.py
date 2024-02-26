from getpass import getpass, getuser

if __name__ == '__main__':
    username = input("Введите логин: ")
    password = getpass("Введите пароль: ")

    print(f"{username} {password}")

    user = getuser()
    print(f"{user=}")
