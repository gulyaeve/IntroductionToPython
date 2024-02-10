#!/home/eugene/PycharmProjects/IntroductionToPython/venv/bin/python
import sys


def main():
    sys.argv.pop(0)
    elements = map(int, sys.argv)
    result = 0
    for element in elements:
        result += element
    return result


if __name__ == '__main__':
    print(main())
