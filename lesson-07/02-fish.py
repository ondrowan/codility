UPSTREAM = 0
DOWNSTREAM = 1


def solution(sizes, directions):
    alive_upstream_fishes = 0
    downstream_fishes = []

    for current_fish_index, current_fish_direction in enumerate(directions):
        # Downstream fishes are always pushed on top of stack
        if current_fish_direction == DOWNSTREAM:
            downstream_fishes.append(current_fish_index)
        else:
            # If there are downstream fishes on stack, iterate over them and eat
            # the smaller ones. If the fish on stack is bigger this one dies and
            # we don't care about it anymore.
            while len(downstream_fishes) != 0:
                if sizes[current_fish_index] > sizes[downstream_fishes[-1]]:
                    downstream_fishes.pop()
                else:
                    break
            # If there are no downstream fishes on stack, this upstream fish
            # will survive and we don't care about it anymore.
            else:
                alive_upstream_fishes += 1

    return alive_upstream_fishes + len(downstream_fishes)


assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution([5, 4, 3, 2, 1], [1, 0, 0, 0, 0]) == 1
assert solution([5, 4, 3, 2, 1], [1, 1, 1, 1, 1]) == 5
assert solution([1, 2, 3, 4, 5], [1, 0, 0, 0, 0]) == 4
assert solution([5, 6, 3, 4, 1], [0, 1, 0, 1, 0]) == 3
assert solution([5, 6, 3, 4, 1], [1, 0, 1, 0, 1]) == 3
assert solution([1], [1]) == 1
assert solution([5, 4, 6], [1, 1, 0]) == 1
