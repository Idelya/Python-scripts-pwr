from typing import Dict, Callable
from students import students_arr, student_type

students_list = students_arr
student_list_helper = []


def print_stud_short_with_key(stud: student_type, key: str) -> None:
    print("STUDENT: ", stud.get('imie'), ' ', stud.get('nazwisko'), ' - ', stud.get(key))


def print_stud(stud: student_type) -> None:
    print("STUDENT")
    for key in stud:
        print(key, ': ', stud.get(key))


def add_student() -> None:
    new_stud = {'imie': '',
                'nazwisko': '',
                'PESEL': '',
                'plec': '',
                'rok_studiow': 0,
                'srednia_ocen': 0.0,
                'kierunek_studiow': ''}

    for key in new_stud:
        value = input(key + ':')
        if key == 'rok_studiow':
            new_stud[key] = int(value)
        elif key == 'srednia_ocen':
            new_stud[key] = float(value)
        else:
            new_stud[key] = value

    print("Added new student:")
    print_stud(new_stud)
    students_list.append(new_stud)


def print_all() -> None:
    for stud in students_list:
        print_stud_short_with_key(stud, 'PESEL')


def print_helper() -> None:
    for stud in student_list_helper:
        print_stud(stud)


def sort_by_avg() -> None:
    global students_list
    students_stud = sorted(students_list, key=lambda k: k['srednia_ocen'])
    for stud in students_stud:
        print_stud_short_with_key(stud, 'srednia_ocen')
    students_list = students_stud


def sort_by_surname() -> None:
    global students_list
    students_stud = sorted(students_list, key=lambda k: k['nazwisko'])
    for stud in students_stud:
        print_stud_short_with_key(stud, 'nazwisko')
    students_list = students_stud


def find_by_pesel() -> None:
    pesel = input('Podaj pesel:')
    filtered_list = filter(lambda k: k['PESEL'] == pesel, students_list)
    for stud in filtered_list:
        print_stud(stud)


def remove_by_pesel() -> None:
    global students_list
    pesel = input('Podaj pesel:')
    filtered_list = filter(lambda k: k['PESEL'] != pesel, students_list)
    students_list = []
    for stud in filtered_list:
        students_list.append(stud)


def copy_by_avg() -> None:
    student_list_helper.clear()
    max_avg = float(input('Max. średnia: '))
    filtered_list = filter(lambda k: k['srednia_ocen'] <= max_avg, students_list)
    for stud in filtered_list:
        student_list_helper.append(stud)
    print_helper()


def exit_menu() -> None:
    quit()


menu: Dict[int, Callable[[], None]] = {
    0: add_student,
    1: print_all,
    2: sort_by_avg,
    3: sort_by_surname,
    4: find_by_pesel,
    5: remove_by_pesel,
    6: copy_by_avg,
    7: print_helper,
    8: exit_menu,
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
