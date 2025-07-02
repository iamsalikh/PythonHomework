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
