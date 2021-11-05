from Inheritance_exercise.animal import Animal


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)