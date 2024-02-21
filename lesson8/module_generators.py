
def my_range(start, stop):
    item = start
    while item < stop:
        yield item
        item += 1


if __name__ == '__main__':
    x = my_range(10, 20)
    for i in x:
        print(i)
