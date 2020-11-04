import datetime
from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str, surname: str, birthdate: datetime.date, pesel: str, faculty: str):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.pesel = pesel
        self.faculty = faculty

    def get_age(self) -> int:
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

    @abstractmethod
    def print_data(self):
        print('{0} {1}, pesel: {2}, age: {3}, faculty: {4}'.format(self.name, self.surname, self.pesel,
                                                                   str(self.get_age()), self.faculty))
