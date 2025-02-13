def solution(numbers, k):
    hash_map = {}

    for num in numbers:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1

    frequency = {}
    for number, count in hash_map.items():
        if count not in frequency:
            frequency[count] = []

        frequency[count].append(number)

    result = []
    for number in reversed(range(len(numbers) + 1)):
        if number in frequency:
            result.extend(frequency[number])

    return result[:k]
