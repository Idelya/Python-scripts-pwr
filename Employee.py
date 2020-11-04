from Person import Person
from abc import ABC


class Employee(Person):
    __metaclass__ = ABC

    def __init__(self, name, surname, birthdate, pesel, faculty, employment_date):
        self.employment_date = employment_date
        super().__init__(name, surname, birthdate, pesel, faculty)

    def print_data(self):
        super(Employee, self).print_data()
        print(self.employment_date)

