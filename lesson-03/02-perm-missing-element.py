import random

def solution(array):
    array.sort()

    if len(array) == 0 or array[0] != 1:
        return 1

    if array[-1] != len(array) + 1:
        return len(array) + 1

    for i, item in enumerate(array, start=0):
        if array[i + 1] - item != 1:
            return item + 1

    return None

assert solution([]) == 1
assert solution([1]) == 2
assert solution([1, 3]) == 2
assert solution([2, 3]) == 1
assert solution([1, 2]) == 3
assert solution([1, 2, 3]) == 4
assert solution([1, 3, 4]) == 2
assert solution([2, 3, 4]) == 1

