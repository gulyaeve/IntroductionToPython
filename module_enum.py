from enum import Enum


class Manufacturers(Enum):
    BMW = "БМВ"
    LADA = "Лада"
    GAZ = "ГАЗ"


for m in Manufacturers:
    print(m.name, m.value)
