"""
Dada uma string codificada, retorne a string decodificada.

A regra de codificação é: k[string_codificada], onde a string_codificada dentro dos colchetes serão repetidas o número de k vezes. O valor de k será sempre um número positivo.

Você deve assumir que as strings de entrada são sempre válidas, sem espaço e os colchetes estão bem formatados.
"""


# O(n)
def solution(str_to_decode):
    str_decoded, _ = parse_str(str_to_decode)
    return str_decoded


def parse_str(str_to_decode, index=0, number=None):
    str_decoded = ""

    while index < len(str_to_decode):
        str = str_to_decode[index]

        if str == "]":
            break

        if str == "[":
            index += 1
            continue

        if str.isdigit():
            if number:
                _number = f"{number}{str}"
            else:
                _number = str

            _number = int(_number)
            number = None

            content, index = parse_str(str_to_decode, index + 1, number=_number)
            str_decoded += content
        else:
            str_decoded += str
            index += 1

    if number:
        str_decoded = str_decoded * number

    return str_decoded, index + 1


def solution(string):
    stack = []

    for i in range(len(string)):
        str_ = string[i]

        if str_ == "[":
            continue

        if str_ == "]":
            last_pop = stack.pop()
            pop = stack.pop()

            if pop.isdigit():
                stack.append(last_pop * int(pop))
            else:
                stack.append(pop + last_pop)

            continue

        if str_.isdigit():
            try:
                last_el = stack[-1]

                if last_el.isdigit():
                    stack.pop()
                    str_ = f"{last_el}{str_}"
            except IndexError:
                pass

        stack.append(str_)
    else:
        while len(stack) > 1:
            last_pop = stack.pop()
            pop = stack.pop()

            if pop.isdigit():
                stack.append(last_pop * int(pop))
            else:
                stack.append(pop + last_pop)

    return stack[0]


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


print(solution("22[a]3[bc]"))
print(solution("3[a2[c]]"))
print(solution("2[abc]3[cd]ef"))

"""
aaaaaaaaaaaaaaaaaaaaaabcbcbc
acccccccccccccccccccccccccccccccc
abcabccdcdcdef

"""
