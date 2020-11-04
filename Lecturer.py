from Employee import Employee
from Observer import Observable, Observer
from typing import List


class Lecturer(Employee, Observable):

    def __init__(self, name, surname, birthdate, pesel, faculty, employment_date, department):
        self.department = department
        self._observers = []
        super().__init__(name, surname, birthdate, pesel, faculty, employment_date)

    def notify(self) -> None:
        for observer in self._observers:
            print(observer)
            observer.update(self)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
        print("New attach" + self.surname + " Observers: " + str(len(self._observers)))

    def set_examine_date(self) -> None:
        input('Add an exam:')
        self.notify()

    def print_data(self):
        print("Lecturer")
        super(Lecturer, self).print_data()
        print("Department:", self.department)
        print("Observers:" + str(len(self._observers)))
