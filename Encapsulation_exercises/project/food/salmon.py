from Encapsulation_exercises.project.food import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self,name, price):
        super().__init__(name, price, Salmon.GRAMS)