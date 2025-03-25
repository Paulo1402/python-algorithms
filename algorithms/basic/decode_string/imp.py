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


if __name__ == "__main__":
    test_data = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ]

    for data in test_data:
        str_to_decode, expected = data
        result = solution(str_to_decode)

        assert result == expected, f"{result} != {expected}"

    print("PASSED")
