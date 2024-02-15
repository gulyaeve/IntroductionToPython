import matplotlib.pyplot as mpl
from numpy.random import shuffle

x = [float(i) for i in range(1, 8)]
shuffle(x)
mpl.plot(x)


if __name__ == '__main__':
    mpl.show()
