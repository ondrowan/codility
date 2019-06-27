def solution(array):
    array.sort()

    while len(array) > 2:
        i1 = array[-1]
        i2 = array[-2]
        i3 = array[-3]

        if (i1 + i2 > i3 and i1 + i3 > i2 and i2 + i3 > i1):
            return 1

        array.pop(-1)

    return 0




assert(solution([10, 2, 5, 1, 8, 20]) == 1)
assert(solution([10, 50, 5, 1]) == 0)
assert(solution([]) == 0)
assert(solution([1]) == 0)
assert(solution([1, 2, 3]) == 0)
assert(solution([1, 1, 1]) == 1)