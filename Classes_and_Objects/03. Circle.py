class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius


    def get_area(self):
        area = self.radius**2 * Circle.pi
        return area

    def get_circumference(self):
        diametur = self.radius * 2
        circumeference = diametur * Circle.pi
        return circumeference


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
