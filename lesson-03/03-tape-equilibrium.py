def solution(array):
    results = []

    head_sum = sum(array[:1])
    tail_sum = sum(array[1:])
    results.append(abs(head_sum - tail_sum))

    start_index = 2

    for index, _ in enumerate(array[start_index:], start=start_index):
        head_sum = head_sum + array[index - 1]
        tail_sum = tail_sum - array[index - 1]

        diff = abs(head_sum - tail_sum)

        if diff == 0:
            return 0

        results.append(diff)

    return min(results)


solution(list(range(2, 100000)))

assert(solution([3, 1]) == 2)
assert(solution([3, 1, 2, 4, 3]) == 1)