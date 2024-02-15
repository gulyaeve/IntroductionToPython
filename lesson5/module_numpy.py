import sys

import numpy as np
from random import shuffle


a_list = [i for i in range(50)]
b_list = [i for i in range(50)]
# shuffle(a_list)
# shuffle(b_list)
a0 = np.array(a_list)
b0 = np.array(b_list)


if __name__ == '__main__':
    c0 = a0 + b0
    print(c0)

    c0 = a0 * b0
    print(c0)
    # print(a, type(a))
    # print(a[1][3])

    a1 = np.arange(0, 2*np.pi, np.pi/6)
    s1 = np.sin(a1)
    for j in range(len(a1)):
        print(a1[j], s1[j])

    a2 = np.linspace(0, 2, 8, False)
    print(a2[1:len(a2):2])
    # print(a1)

    b_list = [i for i in range(50)]
    b0 = np.array(b_list)
    b0[2] += 100
    print(b0)

    mas_0 = np.ones(4)
    print(mas_0, type(mas_0))
    mas_0 = np.zeros(4)
    print(mas_0, type(mas_0))
    mas_0 = np.empty(4)
    print(mas_0, type(mas_0))
    mas_0 = np.full((5, 5), 100)
    print(mas_0, type(mas_0))

    A = np.arange(0, 3000, 1)
    # np.set_printoptions(threshold=sys.maxsize)
    # print(A)

    print(A.sum())
    print(A.mean())
    print(A.min())
    print(A.max())
    print(A.std())

    a_2 = np.array([i for i in range(5)])
    b_2 = np.array([i for i in range(5, 10)])

    c_2 = a_2[:3] + b_2[1:4]
    print(c_2)

    x_1 = np.zeros((2, 3))
    print(x_1)
    y_1 = np.eye(5)
    print(y_1)

    x_2 = np.array(
        [
            [i for i in range(2)],
            [i for i in range(5, 7)]
        ]
    )
    print(x_2)

    print(x_2.sum())
    print(x_2.sum(axis=0))
    print(x_2.sum(axis=1))
    print(x_2.min())
    print(x_2.mean())
    print(x_2.max())
    print(x_2.min(axis=0))
    print(x_2.min(axis=1))

    print("---")
    for element in x_2.flat:
        print(element, end=" ")

    x_3 = np.array(
        [
            [i for i in range(10, 12)],
            [i for i in range(15, 17)]
        ]
    )
    print()
    print(x_2)
    print(x_3)

    print(np.vstack((x_2, x_3)))
    print(np.hstack((x_2, x_3)))

    print(np.hsplit(x_3, 1))
    print(x_3[:, 1])

    print(np.dot(x_2, x_3))

    np.savetxt("mas.txt", np.dot(x_2, x_3))
    r_0 = np.loadtxt("mas.txt")
    print(r_0)
