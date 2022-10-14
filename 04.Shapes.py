from abc import ABC, abstractmethod
import math
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        return

    @abstractmethod
    def calculate_perimeter(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return math.pi * self.radius**2


    def calculate_perimeter(self):
        return 2*math.pi*self.radius



class Rectangle(Shape):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


    def calculate_area(self):
        return self.height * self.weight


    def calculate_perimeter(self):
        return (2*self.height) + (2*self.weight)



circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

