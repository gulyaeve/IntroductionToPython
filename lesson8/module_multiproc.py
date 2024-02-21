import time


def f1():
    print("Функция 1")


def f2():
    print("Функция 2")
    time.sleep(10)
    print("Функция 2 завершена")


def f3():
    print("Функция 3")
    time.sleep(3)
    print("Функция 3 завершена")


if __name__ == '__main__':
    f1()
    f2()
    f3()
