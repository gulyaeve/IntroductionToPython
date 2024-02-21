import time


def long_process():
    for i in range(30000):
        yield i


def timer_5sec():
    time0 = round(time.time())
    while True:
        if (round(time.time()) - time0) % 5 == 0:
            yield "Прошло 5 секунд"
        else:
            yield 0


def main():
    data = long_process()
    timer = timer_5sec()
    while True:
        d = next(data)
        t = next(timer)
        print(d)
        if t:
            print(t)
        time.sleep(1)


if __name__ == '__main__':
    main()
