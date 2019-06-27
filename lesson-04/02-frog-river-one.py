def solution(end_position_index, leave_drops):
    path = [False] * end_position_index

    for index, leave_drop in enumerate(leave_drops, start=0):
        if (leave_drop > len(path)):
            continue

        path[leave_drop - 1] = True

        if all(path):
            return index

    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(solution(1, [1]) == 1)