from Polymorhisym_abstraction.Poly_exercises.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Male')

    def make_sound(self):
        return 'Hiss'

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {__class__.__name__}'