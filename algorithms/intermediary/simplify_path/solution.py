"""
Simplifique o path absoluto para um arquivo (no estilo Unix). Em outras palavras, converta o mesmo para o modo canonico.

Neste modo, o '.' se refere ao diretório atual. '..' se refere ao diretório acima.

Lembre-se que o path neste formato deve sempre começar com '/' e sempre devera ter um '/' único entre os diretórios.

Exemplo 1:
Entrada: "/home/"
Saída: "/home"

Exemplo 2:
Entrada: "/home/../"
Saída: "/"

Exemplo 3:
Entrada: "/home/../home/./"
Saída: "/home"

Exemplo 4:
Entrada: "/home/../home"
Saída: "/home"
"""


def solution(path):
    left = 0
    stack = []

    if path[-1] != "/":
        path += "/"

    for right in range(len(path)):
        if path[right] == "/":
            current = path[left:right]
            left = right

            if current:
                if current == "/..":
                    if stack:
                        stack.pop()
                elif current == "/." or current == "/":
                    continue
                else:
                    stack.append(current)

    if not stack:
        stack.append("/")

    return "".join(stack)


print(solution("/home/"))
print(solution("/home/../"))
print(solution("/home/../home/./"))
print(solution("/home/../home"))
