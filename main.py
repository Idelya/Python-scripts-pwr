import trigonometric
from typing import Callable
from random import randint
import math
INT_APPROXIMATION = 50

# Przyjęto, że użytkownik podaje argument w stopniach


def randomize(fun: Callable[[float, int], float]) -> None:
    for i in range(0, 10):
        n = randint(1, 10)

        text = "Dla argumentu {} {} {}."
        print(text.format(n, 'sin', fun(n, INT_APPROXIMATION)))


def run_app() -> None:
    print('Zad 1')
    degrees_x = float(input('Podaj dla ilu stopni chcesz policzyc sinus:'))
    radian_x = math.radians(degrees_x)
    print(trigonometric.sin(radian_x, INT_APPROXIMATION))
    print('Random sin')
    randomize(trigonometric.sin)
    degrees_z = float(input('Podaj dla ilu stopni chcesz policzyc cosinus:'))
    radian_z = math.radians(degrees_z)
    print(trigonometric.cos(radian_z, INT_APPROXIMATION))
    print('Random cos')
    randomize(trigonometric.cos)


if __name__ == '__main__':
    run_app()
