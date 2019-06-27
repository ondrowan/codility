def solution(number):
    binary = str(bin(number))[2:]

    possible_binary_gap = 0
    binary_gaps = []
    previous_digit = None

    for digit in binary:
        digit = int(digit)

        if digit == 0:
            previous_digit = 0

            if previous_digit == 0:
                possible_binary_gap = possible_binary_gap + 1
            elif previous_digit == 1:
                possible_binary_gap = 1
        else:
            previous_digit = 1
            binary_gaps.append(possible_binary_gap)
            possible_binary_gap = 0

    return max(binary_gaps) if len(binary_gaps) else 0

print(solution(1010101))