from Employee import Employee
from Observer import Observable, Observer
from typing import List


class Lecturer(Employee, Observable):
    __observers: List[Observer] = []
    __exam_list: List[str] = []

    def __init__(self, name, surname, birthdate, pesel, faculty, employment_date, department):
        self.department = department
        super().__init__(name, surname, birthdate, pesel, faculty, employment_date)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self)

    def detach(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def attach(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def set_examine_date(self) -> None:
        exam = input('Add an exam:')
        self.__exam_list.append(exam)
        self.notify()

    def print_data(self):
        print("Lecturer")
        super(Lecturer, self).print_data()
        print("Department:", self.department)
