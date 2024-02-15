from decimal import Decimal
from fractions import Fraction
import math as m
import random


if __name__ == '__main__':
    ...
    # a = Decimal("0.2") - Decimal("0.1") - Decimal("0.1")
    # print(a)
    b = Fraction(6, 4)
    print(b)
    c = Fraction(7, 12)
    print(c)
    d = b * c
    print(d.numerator, d.denominator)
    print(float(d))

    x = 5.75
    y = Fraction(*x.as_integer_ratio())
    print(y)

    print(abs(-54))
    e, f = divmod(12, 7)
    print(e, f)

    print(int("12ab", 12))

    print(min([1, 2, 3]))
    print(max([1, 2, 3]))
    print(sum([1, 2, 3], 1))

    print(round(1.213, 4))
    print(round(1234, -3))

    print(format(1.231312, '^20.3f'))
    print(format(1231312, "_"))

    x = 1_123_321
    print(x)

    print(format(22313132, "^20.3e"))

    print(m.ceil(12313.1))
    print(m.floor(12313.9))

    print(m.fmod(12, 7))

    print(random.random())
    print(random.randint(10, 50))

    a_list = ["Привет", "Здравствуйте", "Hello"]
    random.shuffle(a_list)
    print(a_list)

    print(random.choice(a_list))
    print(random.randrange(10, 50, 4))

    b_list = [i for i in range(100)]
    random.shuffle(b_list)
    print(b_list)
    print(random.sample(b_list, 5))

    a = float('inf')
    print(a)
    a = float('-inf')
    print(a)
    a = float('nan')
    print(a)

    print(m.isnan(a))
    a = [[1, 2], [3, 4]]
