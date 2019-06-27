import math

def solution(start, end, jump_distance):
    distance = end - start

    return math.ceil(distance / jump_distance)

print(solution(3, 999111321, 7))