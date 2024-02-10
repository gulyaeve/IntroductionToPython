# from math import *
# import math
# from module_2 import print_hello
# import module_2

print("Some output from module 1")

if __name__ == '__main__':
    ...
    # print(pow(2.6, 5))
    # print("Hello from module 1")
    # # while True:
    # #     print("Hello from module 1")
    # # for i
    # print(sorted("привет", reverse=True))
    # print(sum([1, 2]))
    # print_hello()
    my_list = ["first", "second", "third", "fourth"]
    MY_LIST = list(map(str.swapcase, my_list))
    print(MY_LIST)
    str1 = "Привет"
    print(list(str1))
    # print(enumerate(my_list))
    for index, item in enumerate(my_list):
        print(f"{index + 1}: {item}")

    my_list = ["first", "second", "third", "fourth"]
    my_list_2 = [1, 2, 3, 4]

    for item, number in zip(my_list, my_list_2):
        print(f"{item = } is a {number = }")

    my_tuple = tuple(my_list)
    # my_tuple += "1"
    print(my_tuple)

    my_list = ["first", "second", "third", "fourth"] * 3
    print(my_list)
    my_set = set(my_list)
    print(my_set)

    my_dict: dict = {
        "key1": "value1",
        "key2": "value2"
    }
    for key, item in my_dict.items():
        print(f"{key}={item}")
    print(my_dict.get("key2"))
    print(list(my_dict.keys()))
    del my_dict['key2']
    print(my_dict.clear())





