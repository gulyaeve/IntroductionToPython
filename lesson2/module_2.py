import math
from typing import Optional, List

# import module_1

name = "Eugene"
surname = "Gulyaev"
x = 1
print(x)


def print_hello(name, surname):
    global x
    x = 3
    # x = 1
    print(f"Hello, {name} {surname}!")
    print(f"Привет, {name} {surname}!")


def multiply(a: int, b: Optional[int] = 1) -> tuple[int, int]:
    """
    Функция для умножения и возведения в степень двух чисел
    :param a: 1 число
    :param b: 2 число
    :return: кортеж с результатами
    """
    print(a * b, a ** b)
    return a * b, a ** b


def my_sum(*args: [int | float]) -> [int | float]:
    summa = 0
    for item in args:
        summa += item
    return summa


if __name__ == '__main__':
    # x = pi
    # y = e
    # print(pi, e)
    # print(sin(120))
    # print(f"{dir()}")
    print(f"{dir(print_hello)}")
    # print(len("11"))
    print_hello(name, surname)
    print(x)
    a1, a2 = multiply(sum([1, 2]), 5)
    # print(type(h))
    print(a1)
    print(a2)
    # x = multiply("Привет", "Пока")
    print(multiply(2))
    q = my_sum(1, 2, 2.5)
    print(len(str(my_sum(1, 2, 2.5))))
