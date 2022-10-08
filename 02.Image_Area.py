class ImageArea:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def __gt__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)


