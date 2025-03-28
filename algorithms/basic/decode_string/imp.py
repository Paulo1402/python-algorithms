def solution(str_to_decode):
    stack = []
    number = 0
    temp_str = ""

    for s in str_to_decode:
        if s == "[":
            if temp_str:
                stack.append(temp_str)
                temp_str = ""

            stack.append(number)
            number = 0
        elif s == "]":
            if temp_str:
                stack.append(temp_str)
                temp_str = ""

            new_str = ""
            first = stack.pop()

            while first and type(first) != int:
                new_str = first + new_str
                first = stack.pop()

            new_str *= first
            stack.append(new_str)
        else:
            if s.isdigit():
                number = 10 * number + int(s)
            else:
                temp_str += s

    if temp_str:
        stack.append(temp_str)

    return "".join(stack)
