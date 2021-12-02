from Inheritance_lectures.employee import Employee
from Inheritance_lectures.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'


