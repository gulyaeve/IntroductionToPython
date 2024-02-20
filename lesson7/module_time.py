import time

if __name__ == '__main__':
    print(time.time())
    print(time.ctime())

    # time.sleep(4.5)
    #
    # print(time.ctime())
    for i in range(1, 10):
        time.sleep(1)
        print(i)


