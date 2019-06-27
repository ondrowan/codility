def has_even_neg_numbers(array):
    neg_num = 0

    for num in array[-3:]:
        if num < 0:
            neg_num = neg_num + 1

    if neg_num == 0:
        return None

    if neg_num % 2 == 0
        return -3

def solution(array):
    sorted_array = sorted(array, key=lambda num: abs(num))

    print(sorted_array)

    while len(sorted_array) >= 3:
        neg = has_even_neg_numbers(sorted_array[-3:])

        if neg is None:
            break



        print(len(sorted_array), has_even_neg_numbers(sorted_array[-3:]))
        sorted_array.pop(-1)

    print(sorted_array)

    return sorted_array[-3:-2][0] * sorted_array[-2:-1][0] * sorted_array[-1:][0]

assert(solution([-3, 1, 2, -2, 5, 6]) == 60)
assert(solution([2, -2, 2]) == -8)
assert(solution([-2, -2, 2]) == 8)