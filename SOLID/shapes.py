from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_are(self):
        pass

class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_are(self):
        return (self.width * self.height) / 2

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_are(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_are(self):
        return 3.14 * self.radius **2

class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_are()

        return total



shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(150)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)