
from Encapsulation_exercises.caretaker import Caretaker
from Encapsulation_exercises.cheetah import Cheetah
from Encapsulation_exercises.keeper import Keeper
from Encapsulation_exercises.lion import Lion
from Encapsulation_exercises.tiger import Tiger
from Encapsulation_exercises.vet import Vet


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []


    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return 'Not enough budget'
        return 'Not enough space for animal'


    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'


    def fire_worker(self,worker_name):
        for man in self.workers:
            if man.name == worker_name:
                self.workers.remove(man)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = 0
        for x in self.workers:
            total_salaries += x.salary

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'


    def tend_animals(self):
        total_pay_animals = 0
        for animal in self.animals:
            total_pay_animals += animal.money_for_care

        if self.__budget >= total_pay_animals:
            self.__budget -= total_pay_animals
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount


    def animals_status(self):

        lions_info = []
        total_lions = 0
        result = f'You have {len(self.animals)} animals\n'
        for kind in self.animals:
           if type(kind) == Lion:
               total_lions += 1
               lions_info.append(repr(kind))


        tiger_info = []
        total_tigers = 0
        for kind in self.animals:
           if type(kind) == Tiger:
               total_tigers += 1
               tiger_info.append(repr(kind))

        cheetah_info = []
        total_cheetah = 0
        for kind in self.animals:
            if type(kind) == Cheetah:
                total_cheetah += 1
                cheetah_info.append(repr(kind))


        result += f'----- {total_lions} Lions:\n'
        lion_result = '\n'.join(lions_info)
        result += lion_result + '\n'

        result += f'----- {total_tigers} Tigers:\n'
        tiger_result = '\n'.join(tiger_info)
        result += tiger_result + '\n'

        result += f'----- {total_cheetah} Cheetahs:\n'
        cheetah_result = '\n'.join(cheetah_info)
        result += cheetah_result

        return result


    def workers_status(self):

        keeper_info = []
        total_keepers = 0
        result = f'You have {len(self.workers)} workers\n'
        for kind in self.workers:
            if type(kind) == Keeper:
                total_keepers += 1
                keeper_info.append(repr(kind))

        vet_info = []
        total_vets = 0
        for kind in self.workers:
            if type(kind) == Vet:
                total_vets += 1
                vet_info.append(repr(kind))

        caretaker_info = []
        total_caretakers = 0

        for kind in self.workers:
            if type(kind) == Caretaker:
                total_caretakers += 1
                caretaker_info.append(repr(kind))

        result += f'----- {total_keepers} Keepers:\n'
        keeper_result = '\n'.join(keeper_info)
        result += keeper_result + '\n'

        result += f'----- {total_caretakers} Caretakers:\n'
        caretaker_result = '\n'.join(caretaker_info)
        result += caretaker_result + '\n'

        result += f'----- {total_vets} Vets:\n'
        vets_result = '\n'.join(vet_info)
        result += vets_result

        return result















