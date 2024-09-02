"""
Dada uma string codificada, retorne a string decodificada.

A regra de codificação é: k[string_codificada], onde a string_codificada dentro dos colchetes serão repetidas o número de k vezes. O valor de k será sempre um número positivo.

Você deve assumir que as strings de entrada são sempre válidas, sem espaço e os colchetes estão bem formatados.
"""

def solution(str_to_decode):
    str_decoded, _ = parse_str(str_to_decode)
    return str_decoded


def parse_str(str_to_decode, index = 0, number = None):
    str_decoded = ''

    while index < len(str_to_decode):
        str = str_to_decode[index]

        if str == ']':
            break

        if str == '[':
            index += 1
            continue

        if str.isdigit():
            content, index = parse_str(str_to_decode, index + 1, number=int(str))
            str_decoded += content
        else:
            str_decoded += str
            index += 1

    if number:
        str_decoded = str_decoded * number

    return str_decoded, index + 1


print(solution('2[a]3[bc]'))
print(solution('3[a2[c]'))
print(solution('2[abc]3[cd]ef'))