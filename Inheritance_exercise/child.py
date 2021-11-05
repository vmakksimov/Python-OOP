from Inheritance_exercise.person import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return self




