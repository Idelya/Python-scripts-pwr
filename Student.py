from Observer import Observer, Observable
from Person import Person


class Student(Person, Observer):

    def __init__(self, name, surname, birthdate, pesel, faculty, index):
        self.index = index
        super().__init__(name, surname, birthdate, pesel, faculty)

    def update(self, observable: Observable) -> None:
        print("Student" + self.name + ' ' + self.surname + ' ' + self.pesel + ' ' + self.faculty + ' - notified')

    def print_data(self):
        print("Student")
        super(Student, self).print_data()
        print("index:", self.index)
