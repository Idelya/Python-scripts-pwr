from typing import Dict, Callable, List
from Model.Person import Person
import datetime

pwr_list: List[Person] = []
pwr_list_helper: List[Person] = []


menuAdd: Dict[int, Callable[[], Person]] = {
    0: lambda: print(pwr_list),
    1: lambda: print(pwr_list),
    2: lambda: print(pwr_list),
}

def add_person() -> None:
    for key in menuAdd:
        print(key, '=>', menuAdd[key].__name__)

    option = input('select from menu:')
    if not option.isnumeric():
        print('You have to pick a number.')
    else:
        name = input('Name:')
        surname = input('Surname:')
        birthday = datetime.datetime.strptime(input('Birthdate (yyyy-mm-dd):'), '%Y-%m-%d').date()
        pesel = input('Pesel:')
        faculty = input('Faculty:')

        new_person = menuAdd.get(int(option))(name, surname, birthday, pesel, faculty)
        pwr_list.append(new_person)

