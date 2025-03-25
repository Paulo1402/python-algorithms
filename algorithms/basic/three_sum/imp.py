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

    result.sort()

    return result
