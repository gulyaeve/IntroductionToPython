import sys

name = input("Введите ваше имя: ")
# age = int(input("Введите возраст: "))
age = input("Введите возраст: ")

# if age.isdigit():
#     print(f"Вау, мне тоже {age} лет")
# else:
#     print("Вводите возраст числом, пожалуйста")
#     sys.exit()

while not age.isdigit():
    print("Вводите возраст числом, пожалуйста")
    age = input("Введите возраст: ")

if age.endswith("1"):
    print(f"Вау, мне тоже {age} год")
elif age.startswith("1") and len(age) == 2:
    print(f"Вау, мне тоже {age} лет")
elif age.endswith(("2", "3", "4")):
    print(f"Вау, мне тоже {age} года")
else:
    print(f"Вау, мне тоже {age} лет")

print(f"Вас зовут {name}")

