from typing import List, Dict, Union, TypedDict

student_type = TypedDict("student_type", {
    'imie': str,
    'nazwisko': str,
    'PESEL': str,
    'plec': str,
    'rok_studiow': int,
    'srednia_ocen': float,
    'kierunek_studiow': str,
})

students_arr: List[student_type] = [{
    'imie': 'Agata',
    'nazwisko': 'Walerczyk',
    'PESEL': '98031359375',
    'plec': 'K',
    'rok_studiow': 4,
    'srednia_ocen': 4.23,
    'kierunek_studiow': 'Zarzadzanie'
},
{
    'imie': 'Michal',
    'nazwisko': 'Koszyk',
    'PESEL': '99090365372',
    'plec': 'M',
    'rok_studiow': 2,
    'srednia_ocen': 2.23,
    'kierunek_studiow': 'Zarzadzanie'
},
{
    'imie': 'Lucjan',
    'nazwisko': 'Kowalczyk',
    'PESEL': '991018590374',
    'plec': 'M',
    'rok_studiow': 3,
    'srednia_ocen': 3.75,
    'kierunek_studiow': 'Informatyka'
},
{
    'imie': 'Jakub',
    'nazwisko': 'Treczyk',
    'PESEL': '00100649938',
    'plec': 'M',
    'rok_studiow': 1,
    'srednia_ocen': 5.03,
    'kierunek_studiow': 'Informatyka'
},
{
    'imie': 'Ewelina',
    'nazwisko': 'Malarcz',
    'PESEL': '99021679675',
    'plec': 'K',
    'rok_studiow': 3,
    'srednia_ocen': 4.53,
    'kierunek_studiow': 'Zarzadzanie'
},{
    'imie': 'Joanna',
    'nazwisko': 'Kruk',
    'PESEL': '99022674947',
    'plec': 'K',
    'rok_studiow': 4,
    'srednia_ocen': 4.23,
    'kierunek_studiow': 'Informatyka'
},{
    'imie': 'Agata',
    'nazwisko': 'Roczek',
    'PESEL': '96050458429',
    'plec': 'K',
    'rok_studiow': 4,
    'srednia_ocen': 3.34,
    'kierunek_studiow': 'Zarzadzanie'
},
{
    'imie': 'Hubert',
    'nazwisko': 'Gil',
    'PESEL': '98031954332',
    'plec': 'M',
    'rok_studiow': 2,
    'srednia_ocen': 4.83,
    'kierunek_studiow': 'Informatyka'
},{
    'imie': 'Filip',
    'nazwisko': 'Dryń',
    'PESEL': '00031359374',
    'plec': 'M',
    'rok_studiow': 1,
    'srednia_ocen': 4.5,
    'kierunek_studiow': 'Informatyka'
},{
    'imie': 'Paulina',
    'nazwisko': 'Kwaitkowska',
    'PESEL': '99111132145',
    'plec': 'K',
    'rok_studiow': 4,
    'srednia_ocen': 4.93,
    'kierunek_studiow': 'Informatyka'
}]