def solution(numbers, target_sum):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return [numbers[i], numbers[j]]

    return []
