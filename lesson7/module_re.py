import re

if __name__ == '__main__':
    txt = "Привет, мир! Привет, мир!"
    x = re.search(r"^Привет.*!$", txt)
    print(x)

    x = re.findall(r"М", txt)
    print(x)

    x = re.search(r"\s", txt)
    print(x.start())

    x = re.split(r"\s", txt, 2)
    print(x)

    x = re.sub(r"\s", ".", txt, 2)
    print(x)

    x = re.match(r"^Привет.*!$", txt)
    print(x)
