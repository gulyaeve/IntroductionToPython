class GreaterThanFiveError(Exception):
    pass


if __name__ == '__main__':
    my_d = {"1": 1, "2": 2}
    for i in range(-10, 10):
        try:
            if i > 5:
                raise GreaterThanFiveError
            # print(my_d['3'])
            assert i > -2, "Значения меньше -2 не подходят"
            print(f"{i} -- {10 / i}")
            # print('10' + 10)
            if i == 7:
                raise ValueError("7 нам не нужны")
        except ZeroDivisionError:
            print("На 0 делить нельзя")
        except (TypeError, KeyError):
            print("Сложение несовместимых типов или не тот ключ")
        except Exception as e:
            print(f"Неизвестное исключение: {e} {type(e)}")
        finally:
            print("Вывод в любом случае")
