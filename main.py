# Числовые типы
# a: float = 1.5
b: int = 3
# s = a + b
# print(s)

c: complex = 1+3j
c2 = complex(2, 3)
print(c2)

# Строки
s: str = "Союз Сове Соци Рес"
print(f"{s[1::5]=}")
new_s = s.center(100)
str_f = f"Значение комплексной переменной: {c2}"
str_f2 = "a = {}"
print(new_s)
print(str_f)
print(str_f2.format(b))
print("-" * 20)
str_with_int = "3"
x = int(str_with_int) + 2
print(f"{x=}")

#  Списки
new_list: list = s.split()
empty_string = ""
for i in new_list:
    empty_string += i[0]
print(new_list)
print(empty_string)

# e = int(input("Введите e: "))
e = 3
# condition = e > 3 and not (e <= 20 or e == 25)
# if condition:
#     print("e lower than 20 and greater than 3")
if e > 3:
    print("e больше 3")
elif e < 3:
    print("e меньше 3")
else:
    print("e равно 3")
print("Вывод после условия")

# Списки
list2: list = [1, 2, 3, "Name", ["1_2", "2_2"]]
print(f"Before {list2 = }")
# list2.append(45)
# list2[4].pop(1)
list3 = list2.copy()
# list3.pop(1)
# list3.insert(2, "New name")
list3.append(3)
# list3 = list3.count(3)
list3.reverse()
print(f"After {list2 = } \nAfter {list3 = }")
