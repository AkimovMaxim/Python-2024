import math

class Shape:
    def area(self):
        raise NotImplementedError("Этот метод прописан в подклассе")

    def perimeter(self):
        raise NotImplementedError("Этот метод прописан в подклассе")

    def __str__(self):
        return self.__class__.__name__

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"{super().__str__()}(radius={self.radius})"

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.sides = [a, b, c]

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

    def perimeter(self):
        return sum(self.sides)

    def __str__(self):
        return f"{super().__str__()}(sides={self.sides})"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{super().__str__()}(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"{super().__str__()}(side={self.width})"

class Rhombus(Shape):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2

    def perimeter(self):
        side = math.sqrt((self.diagonal1 / 2) ** 2 + (self.diagonal2 / 2) ** 2)
        return 4 * side

    def __str__(self):
        return f"{super().__str__()}(diagonal1={self.diagonal1}, diagonal2={self.diagonal2})"


circle = Circle(5)
triangle = Triangle(3, 4, 5)
rectangle = Rectangle(2, 3)
square = Square(4)
rhombus = Rhombus(6, 8)
