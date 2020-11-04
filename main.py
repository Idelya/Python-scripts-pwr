from typing import Dict, Callable, List
from Student import Student
from Person import Person
from Administration import Administration
from Lecturer import Lecturer
import pickle
import datetime

pwr_list: List[Person] = []
pwr_list_helper: List[Person] = []


def add_person() -> None:
    for key in menuAdd:
        print(key, '=>', menuAdd[key].__name__)

    option = input('select from menu:')
    if not option.isnumeric():
        print('You have to pick a number.')
    elif int(option) in menu:
        name = input('Name:')
        surname = input('Surname:')
        birthday = datetime.datetime.strptime(input('Birthday:'), '%Y-%m-%d').date()
        pesel = input('Pesel:')
        faculty = input('Faculty:')

        new_person = menuAdd.get(int(option))(name, surname, birthday, pesel, faculty)
        pwr_list.append(new_person)
    else:
        print('Option not found.')


def add_student(name: str, surname: str, birthday: datetime.date, pesel: str, faculty: str) -> Student:
    index = input('Index:')
    stud = Student(name, surname, birthday, pesel, faculty, index)

    filtered_list = filter(lambda k: k.faculty == faculty, pwr_list)
    for lecturer in filtered_list:
        lecturer.attach(stud)

    return stud


def add_administration(name: str, surname: str, birthday: datetime.date, pesel: str, faculty: str) -> Administration:
    empoyment_date = input("Date of employment:")
    office = input("Office:")
    return Administration(name, surname, birthday, pesel, faculty, empoyment_date, office)


def add_lecturer(name: str, surname: str, birthday: datetime.date, pesel: str, faculty: str) -> Lecturer:
    empoyment_date = input("Date of employment:")
    department = input("Department:")
    lecturer = Lecturer(name, surname, birthday, pesel, faculty, empoyment_date, department)

    filtered_list = filter(lambda k: k.faculty == faculty, pwr_list)
    for stud in filtered_list:
        lecturer.attach(stud)
    return lecturer


def print_all() -> None:
    for person in pwr_list:
        person.print_data()


def print_helper() -> None:
    for person in pwr_list_helper:
        person.print_data()


def sort_by_age() -> None:
    pwr_list.sort(key=lambda k: k.get_age())
    print_all()


def sort_by_surname() -> None:
    pwr_list.sort(key=lambda k: k.surname)
    print_all()


def find_by_pesel_and_print() -> None:
    person = find_by_pesel()
    person.print_data()


def find_by_pesel() -> Person:
    pesel = input('Podaj pesel:')
    filtered_list = filter(lambda k: k.pesel == pesel, pwr_list)
    for person in filtered_list:
        return person


def to_remove(pesel: str) -> None:
    filtered_list = filter(lambda k: k.pesel == pesel, pwr_list)
    for person in filtered_list:
        if type(person) is Student:
            observable_list = filter(lambda k: k.faculty == person.faculty, pwr_list)
            for lecturer in observable_list:
                lecturer.detach(person)
        if type(person) is Lecturer:
            observer_list = filter(lambda k: k.faculty == person.faculty, pwr_list)
            for lecturer in observer_list:
                person.detach(lecturer)


def remove_by_pesel() -> None:
    global pwr_list
    filtered_list = find_by_pesel()
    pwr_list = []
    for stud in filtered_list:
        pwr_list.append(stud)


def copy_by_age() -> None:
    pwr_list_helper.clear()
    max_age = float(input('Max. age: '))
    filtered_list = filter(lambda k: k.get_age() <= max_age, pwr_list)
    for stud in filtered_list:
        pwr_list_helper.append(stud)
    print_helper()


def save_list() -> None:
    file_name = input("File name:")
    pickle.dump(pwr_list, open(file_name + '.p', "wb"))


def fetch_data() -> None:
    file_name = input("File name:")
    try:
        new_list = pickle.load(open(file_name + '.p', "rb"))
        for person in new_list:
            pwr_list.append(person)
    except EOFError:
        print("File empty")
    except FileNotFoundError:
        print("File not found")


def create_exam() -> None:
    lecturer = find_by_pesel()
    if type(lecturer) is Lecturer:
        lecturer.set_examine_date()
    else:
        print("Wrong pesel")


def exit_menu() -> None:
    quit()


menuAdd: Dict[int, Callable[[], Person]] = {
    0: add_student,
    1: add_administration,
    2: add_lecturer,
}

menu: Dict[int, Callable[[], None]] = {
    0: add_person,
    1: print_all,
    2: sort_by_age,
    3: sort_by_surname,
    4: find_by_pesel_and_print,
    5: remove_by_pesel,
    6: copy_by_age,
    7: print_helper,
    8: save_list,
    9: fetch_data,
    10: create_exam,
    11: exit_menu,
}


def run_app() -> None:
    while True:
        for key in menu:
            print(key, '=>', menu[key].__name__)
        option = input('select from menu:')
        if not option.isnumeric():
            print('You have to pick a number.')
        elif int(option) in menu:
            menu.get(int(option))()
        else:
            print('Option not found. Please, pick again.')


if __name__ == '__main__':
    run_app()
