def solution(array):
    odd_values = set()

    for value in array:
        if value in odd_values:
            odd_values.remove(value)
        else:
            odd_values.add(value)

    return odd_values.pop()

print(solution([1, 2, 2, 1, 2]))