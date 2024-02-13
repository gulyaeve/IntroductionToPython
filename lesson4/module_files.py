

a = ["name1", "name2", "name3"]
# file = open("text.txt", 'a')
# file2 = open("text2.txt", "w")
# print(a, sep="\n", file=file2)


if __name__ == '__main__':
    ...
    # print(a, sep="\n", file=file2)
    # file2_bytes = open("text2.txt", "rb")
    # print(file2_bytes)
    # file = open("text", encoding="utf-8")
    # print(file.closed, file.name, file.mode)
    # file.close()
    # print(file.closed)

    # file.close()
    # file2.close()
    # file.writelines(["Any string 4", "12345"])
    # file = open("text.txt")
    # for line in file.readlines():
    #     print(line)
    with open("text3.txt", "w") as file:
        [file.write(f"{index + 1}) {line}\n") for index, line in enumerate(a)]

    with open("text3.txt") as file:
        print(file.read())

        # for index, line in enumerate(a):
        #     file.write(f"{index}) {line}\n")

