def solution(string):
    stack = []
    brackets = {
        "}": "{",
        "]": "[",
        ")": "(",
    }

    for letter in string:
        if letter in brackets.values():
            stack.append(letter)

        if letter in brackets.keys():
            if not len(stack):
                return 0

            if stack.pop(-1) != brackets[letter]:
                return 0

    if len(stack):
        return 0

    return 1

assert solution("") == 1
assert solution("{[()()]}") == 1
assert solution("([)()]") == 0
assert solution("}") == 0
assert solution("{") == 0