import sys
import subprocess


if __name__ == '__main__':
    # print(sys.argv)
    # print(sys.exec_prefix)
    # print(sys.executable)

    # output = subprocess.check_output("ls")
    x = subprocess.run("pwd", shell=True, capture_output=True).stdout.decode()
    print(x)

    # with subprocess.Popen(["id"], stdout=subprocess.PIPE) as process:
    #     files = process.stdout.read().decode().split(" ")
    #     print(files)


