import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    PI = math.pi

    def __init__(self, radius):
        self.__radius = radius

    def calculate_perimeter(self):
        return 2 * self.PI * self.__radius

    def calculate_area(self):
        return self.PI * self.__radius ** 2


class Rectangle(Shape):

    def __init__(self, height, width):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)




circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
