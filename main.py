from typing import List, Dict, Callable, Union
from students import students_arr


def add_student():
    pass


def print_all():
    pass


def sort_by_avg():
    pass


def sort_by_surname():
    pass


def find_by_pesel():
    pass


def remove_by_pesel():
    pass


def copy_deep():
    pass


def copy():
    pass


def exit_menu():
    quit()


menu: Dict[int, Union[Callable[[],None], Callable[[],None], Callable[[],None], Callable[[],None]]] = {
    0: add_student,
    1: print_all,
    2: sort_by_avg,
    3: sort_by_surname,
    4: find_by_pesel,
    5: remove_by_pesel,
    6: copy_deep,
    7: copy,
    8: exit_menu,
}


def run_app():
    while True:
        for key in sorted(menu):
            print(key, '=>', menu[key].__name__)
        option = input('select from menu:')
        if not option.isnumeric():
            print('You have to pick a number.')
        elif int(option) in menu:
            print('done')
        else:
            print('Option not found. Please, pick again.')


if __name__ == '__main__':
    run_app()

