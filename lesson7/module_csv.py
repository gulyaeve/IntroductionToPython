import csv


if __name__ == '__main__':
    with open("addresses.csv", "r", newline="\n") as file:
        reader = csv.reader(file)
        for line in reader:
            print(line)
