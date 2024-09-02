"""
O Two Sum é bastante comum durante entrevistas. Seu objetivo é identificar um par de números que somados batam com o valor da variável target.

Ele pode ser escrito em um algoritmo que roda no tempo O(n).

Exemplo:

Se o array é [4, 1, 2, -2, 11, 15, 1, -1, -6, -4] e o target é 9. Neste caso, seu programa deve retornar:

[-2, 11]

O motivo é bastante simples:

-2 + 11 = 9
"""

# Solução 1
def two_sum(numbers, target_sum):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return [numbers[i], numbers[j]]

    return []

# Solução 2
def two_sum(numbers, target_sum):
    hash_table = {}

    for n in numbers:
        y = target_sum - n

        if y in hash_table:
            return [y, n]
        else:
            hash_table[n] = True

    return []

# Solução 3
def two_sum(numbers, target_sum):
    numbers.sort()
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target_sum:
            return [numbers[left], numbers[right]]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return []