from abc import abstractmethod


class Shape:

    @abstractmethod
    def draw(self): ...


class Circle(Shape):
    # radius: int

    def __init__(self, radius: int):
        self.radius = radius

    def draw(self):
        print(f"Круг радиусa {self.radius}")


class Square(Shape):
    # a: int

    def __init__(self, a: int):
        self.a = a

    def draw(self):
        print(f"Квадрат со сторонами {self.a}x{self.a}")


class Triangle(Shape):
    # a: int
    # b: int
    # c: int

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f"Треугольник состоронами {self.a},{self.b},{self.c}")


x = Shape()
x.draw()
shapes = list()
shapes.append(Circle(1))
shapes.append(Triangle(3, 5, 7))
shapes.append(Square(7))

for a in shapes:
    a.draw()
