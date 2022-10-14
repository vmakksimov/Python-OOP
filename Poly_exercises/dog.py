from Polymorhisym_abstraction.Poly_exercises.animal import Animal


class Dog(Animal):
    pass

    def make_sound(self):
        return 'Woof!'


    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {__class__.__name__}'
