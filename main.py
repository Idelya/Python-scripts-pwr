from tkinter import Tk
from typing import Dict, Callable, List

from Model.Student import Student
from Model.Person import Person
from Model.Administration import Administration
from Model.Lecturer import Lecturer
import pickle
import datetime

from View.MainView import MainView


class Storage:
    pwr_list: List[Person] = []
    pwr_list_helper: List[Person] = []

    def add_student(self, name: str, surname: str, birthday: datetime.date, pesel: str, faculty: str, index: str) -> Student:
        stud = Student(name, surname, birthday, pesel, faculty, index)
        self.pwr_list.append(stud)
        self.print_all()

    def add_administration(self, name: str, surname: str, birthday: datetime.date, pesel: str, employment_date: datetime.date, office:str,
                           faculty: str) -> Administration:
        admin = Administration(name, surname, birthday, pesel, faculty, employment_date, office)
        self.pwr_list.append(admin)
        self.print_all()

    def add_lecturer(self, name: str, surname: str, birthday: datetime.date, pesel: str, faculty: str, empoyment_date: datetime.date,
                     department: str) -> Lecturer:
        lecturer = Lecturer(name, surname, birthday, pesel, faculty, empoyment_date, department)
        self.pwr_list.append(lecturer)
        self.print_all()

    def print_all(self) -> None:
        for person in self.pwr_list:
            person.print_data()

    def print_helper(self) -> None:
        for person in self.pwr_list_helper:
            person.print_data()

    def sort_by_age(self) -> None:
        self.pwr_list.sort(key=lambda k: k.get_age())
        self.print_all()

    def sort_by_surname(self) -> None:
        self.pwr_list.sort(key=lambda k: k.surname)
        self.print_all()

    def find_by_pesel_and_print(self, pesel) -> None:
        person = self.find_by_pesel(pesel)
        person.print_data()

    def find_by_pesel(self, pesel) -> Person:
        filtered_list = filter(lambda k: k.pesel == pesel, self.pwr_list)
        for person in filtered_list:
            return person

    def remove_by_pesel(self, pesel) -> None:
        person = self.find_by_pesel(pesel)
        person.print_data()
        filtered_list = filter(lambda k: k.pesel != person.pesel, self.pwr_list)
        self.pwr_list = []
        for stud in filtered_list:
            self.pwr_list.append(stud)

    def copy_by_age(self, max_age) -> None:
        self.pwr_list_helper.clear()
        filtered_list = filter(lambda k: k.get_age() <= max_age, self.pwr_list)
        for stud in filtered_list:
            self.pwr_list_helper.append(stud)
        self.print_helper()

    def save_list(self, file_name) -> None:
        pickle.dump(self.pwr_list, open(file_name + '.p', "wb"))

    def fetch_data(self, file_name) -> None:
        try:
            f = open(file_name, "rb")
            new_list = pickle.load(f)
            for person in new_list:
                self.pwr_list.append(person)
            f.close()
        except EOFError:
            print("File empty")
        except FileNotFoundError:
            print("File not found")


def run_app() -> None:
    storage = Storage()
    app = MainView(storage)
    app.mainloop()


if __name__ == '__main__':
    run_app()
