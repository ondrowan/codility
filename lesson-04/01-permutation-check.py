def solution(array):
    return int(set(array) == set(range(1, len(array) + 1)))

assert(solution([2]) == 0)
assert(solution([1]) == 1)
assert(solution([4, 1, 3, 2]) == 1)
assert(solution([4, 1, 3]) == 0)
assert(solution([3, 2]) == 0)
assert(solution([2, 2]) == 0)
assert(solution([9, 5, 7, 3, 2, 7, 3, 1, 10, 8]) == 0)