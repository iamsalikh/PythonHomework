# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2 
    
    def perimetr(self):
        return 2 * 3.14 * self.radius

# 2. Person Class
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth 
        
    def get_age(self):
        return f"{self.name} from {self.country} is {2025 - self.date_of_birth} years old."

# 3. Calculator Class
class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль"

# 4. Shape and Subclasses
class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a  # сторона 1
        self.b = b  # сторона 2
        self.c = c  # сторона 3

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Формула Герона
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side
