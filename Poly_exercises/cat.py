from Polymorhisym_abstraction.Poly_exercises.animal import Animal


class Cat(Animal):
    pass

    def make_sound(self):
        return 'Meow meow!'


    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {__class__.__name__}'