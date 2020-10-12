import trigonometric
from math_functions import find_max, find_min, average
from typing import Callable, List
from random import randint
import math
INT_PRECISION = 50

# Przyjęto, że użytkownik podaje argument w stopniach


def random_list(a: int, b: int, length: int) -> List[int]:
    arr = []
    for i in range(0, length):
        arr.append(randint(a, b))
    return arr


def randomize(fun: Callable[[float, int], float]) -> None:
    text = "Dla argumentu {} {} {}."
    for i in random_list(1, 10, 10):
        print(text.format(i, 'sin', fun(i, INT_PRECISION)))


def run_app() -> None:
    print('Zad 1')
    degrees_x = float(input('Podaj dla ilu stopni chcesz policzyc sinus:'))
    radian_x = math.radians(degrees_x)
    print(trigonometric.sin(radian_x, INT_PRECISION))
    print('Random sin')
    randomize(trigonometric.sin)
    degrees_z = float(input('Podaj dla ilu stopni chcesz policzyc cosinus:'))
    radian_z = math.radians(degrees_z)
    print(trigonometric.cos(radian_z, INT_PRECISION))
    print('Random cos')
    randomize(trigonometric.cos)

    print('Zad 2')
    arr = random_list(1, 100, 10)
    print('Min: {}'.format(find_min(arr)))
    print('Max: {}'.format(find_max(arr)))
    print('Average: {}'.format(average(arr)))


if __name__ == '__main__':
    run_app()
