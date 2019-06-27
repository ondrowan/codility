from collections import deque

def solution(array, cycles):
    if len(array) == 0:
        return []

    new_list = array

    for _ in range(cycles):
        queue = deque(new_list)
        queue.appendleft(de.pop())

        new_list = list(de)

    return new_list