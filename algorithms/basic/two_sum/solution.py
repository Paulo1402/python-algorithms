# Solução 1 O(n²)
def solution(numbers, target_sum):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return [numbers[i], numbers[j]]

    return []


# Solução 2 O(n)
def solution(numbers, target_sum):
    hash_table = {}

    for n in numbers:
        y = target_sum - n

        if y in hash_table:
            return [y, n]
        else:
            hash_table[n] = True

    return []


# Solução 3 O(n log(n))
def solution(numbers, target_sum):
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
