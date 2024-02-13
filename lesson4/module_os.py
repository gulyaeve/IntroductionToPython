import os


if __name__ == '__main__':
    ...
    # print(os.getcwd())
    # os.chdir("/home/eugene")
    # print(os.getcwd())
    print(os.listdir())
    # # os.mkdir("new folder")
    # # print(os.listdir())
    # os.chdir("new folder")
    # # print(f"{os.path.isdir('.')=}")
    # print(f"{os.path.split(os.getcwd())=}")
    print(os.name)
    print(os.environ)
    print(os.getlogin())
    print(os.getpid())
    print(os.getenv("PATH"))
    print(os.getuid())
    print(os.uname())
    print(os.access(os.getcwd(), os.W_OK))
    print(os.access("/etc", os.W_OK))
    # print(os.makedirs("new/new1/new2"))
    # print(os.removedirs("new/new1/new2"))
    output = os.system("id")
    print(output)
    # with open("user.txt", "w") as file:
    #     file.write(output)




