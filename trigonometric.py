import math
from typing import Callable


def compute_sin(x: float, k: int) -> float:
    sign = math.pow(-1, k)
    return sign * math.pow(x, 2 * k + 1) / math.factorial(2 * k + 1)


def compute_cos(x: float, k: int) -> float:
    sign = math.pow(-1, k)
    return sign * math.pow(x, 2 * k) / math.factorial(2 * k)


def approximates(x: float, precision: int, trig_fun: Callable[[float, int], float]) -> float:
    sin_sum: float = 0
    for i in range(precision):
        sin_sum += trig_fun(x, i)
    return sin_sum


def cos(x: float, precision: int) -> float:
    return approximates(x, precision, compute_cos)


def sin(x: float, precision: int) -> float:
    return approximates(x, precision, compute_sin)
