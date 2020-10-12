from typing import List, Optional


def find_max(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    max_elem = arr[0]
    for i in arr:
        if i > max_elem:
            max_elem = i
    return max_elem


def find_min(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    min_elem = arr[0]
    for i in arr:
        if i < min_elem:
            min_elem = i
    return min_elem


def average(arr: List[int]) -> float:
    if len(arr) == 0:
        return 0
    sum_elem = 0
    for i in arr:
        sum_elem += i
    return sum_elem/len(arr)
