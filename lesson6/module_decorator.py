from functools import wraps


def my_decorator(f: callable):
    print("Вызов в декораторе")
    return f * 2


def my_decorator_2(f: callable):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f"{f(args, **kwargs)}"
    return wrapper


@my_decorator_2
def my_func(x: int):
    return x * 2


if __name__ == '__main__':
    y = my_func(2)
    print(y)
