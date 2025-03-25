# O(n)
def solution(str_to_validate):
    open_chars = []
    close_chars = []

    closing_chars = {"(": ")", "{": "}", "[": "]"}

    for s in str_to_validate:
        # check if s is an opening char
        if s in closing_chars.keys():
            open_chars.append(s)
        # check if s in a closing char
        elif s in closing_chars.values():
            try:
                if open_chars[len(close_chars)] not in closing_chars.keys():
                    return False
            except IndexError:
                return False

            close_chars.append(s)

    if len(open_chars) != len(close_chars):
        return False

    for i in range(len(open_chars)):
        open_char = open_chars[i]
        close_char = close_chars[len(open_chars) - (i + 1)]
        expected_close_char = closing_chars[open_char]

        if close_char != expected_close_char:
            return False

    return True


# O(n)
def solution(str_to_validate):
    mapping = {")": "(", "}": "{", "]": "["}

    stack = []

    for s in str_to_validate:
        if s in mapping:
            if not stack:
                return False

            char = stack.pop()

            if char != mapping[s]:
                return False
        elif s in mapping.values():
            stack.append(s)

    return len(stack) == 0


print(solution("([])"))
print(solution("([{}])"))
print(solution("([{})"))
print(solution("(}])"))
print(solution("(])"))
print(solution(")("))
print(solution("(){}[]"))
