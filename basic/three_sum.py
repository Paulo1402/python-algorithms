"""
O Three sum é uma variação do problema Two Sum, caso você ainda não tenha feito ele sugiro que vá primeiro nele e depois volte aqui.

A idéia deste problema é identificar todos os três números que quando somados resultem em um valor especificado.

Exemplo:

Se o array é [12, 3, 1, 2, -6, 5, -8, 6] e o target é 0. Neste caso, seu programa deve retornar:

[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]

A soma de todos os valores das listas acima será igual a zero.
"""


# O(n³)
def solution(numbers, target_sum):
    result = []

    for i in range(len(numbers) - 2):
        first = numbers[i]

        for j in range(i + 1, len(numbers) - 1):
            second = numbers[j]

            for k in range(j + 1, len(numbers)):
                third = numbers[k]

                if first + second + third == target_sum:
                    result.append(sorted([first, second, third]))

    return result


# O (n²) - O(n)
def solution(numbers, target_sum):
    result = []
    numbers = sorted(numbers)

    for current in range(len(numbers)):
        left = current + 1
        right = len(numbers) - 1

        while left < right:
            sum = numbers[current] + numbers[left] + numbers[right]

            if sum < target_sum:
                left += 1
            elif sum > target_sum:
                right -= 1
            else:
                result.append([numbers[current], numbers[left], numbers[right]])

                left += 1
                right -= 1

    return result


print(solution([12, 3, 1, 2, -6, 5, -8, 6], 0))
