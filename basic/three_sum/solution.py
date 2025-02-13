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
