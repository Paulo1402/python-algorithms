"""
Neste desafio você deverá construir uma função que recebe uma string e identifique se a mesma é uma palindrome, ou seja, se a string é igual a ela mesma invertida.

Exemplo:

Dado que temos a string algomania uma vez invertida temos ainamogla que são diferentes.

Logo, não é uma palindrome.

Ja se recebemos a string abccba uma vez invertida temos abccba que são iguais e a função deve retornar True nesta situação.
"""

def solution(string):
    temp_str = ''
    string = string.lower()

    for i in range(len(string) - 1, -1, -1):
      temp_str += string[i]

    return temp_str == string


def solution(string):
    reversed_index = len(string) - 1

    for index in range(len(string)):
        if index == reversed_index:
            return True

        if string[index] != string[reversed_index]:
            return False

        reversed_index -= 1

    return True
