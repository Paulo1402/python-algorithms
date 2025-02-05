"""
Dado um array que nunca é vazio, retorne os K elementos mais frequentes do mesmo.

Exemplo:

Entrada: [1, 1, 1, 3, 3, 5, 6, 7, 8, 9, 10] -> K = 2

Saída: [1, 3]

Explicação: Os 2 números mais frequentes são 1 e 3.
"""

import heapq


# O(n)
def solution(numbers, k):
    numbers_count = {}

    for number in numbers:
        if number not in numbers_count:
            numbers_count[number] = 0

        numbers_count[number] += 1

    most_frequent_numbers = [
        {"number": number, "count": count} for number, count in numbers_count.items()
    ]
    most_frequent_numbers.sort(key=lambda x: x["count"], reverse=True)

    most_frequent_numbers = [number["number"] for number in most_frequent_numbers[0:k]]

    return most_frequent_numbers


# O(n log n)
def solution(numbers, k):
    hash_map = {}

    for num in numbers:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1

    pairs = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

    result = []
    for pair in pairs[:k]:
        result.append(pair[0])

    return result


# O(n log k)
def solution(numbers, k):
    hash_map = {}

    for num in numbers:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1

    heap = []
    for number, count in hash_map.items():
        heapq.heappush(heap, (count, number))

        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    for pair in heap:
        result.append(pair[1])

    return result


# O(n)
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


print(solution([1, 1, 1, 3, 3, 5, 6, 7, 8, 9, 10], k=2))
print(solution([1, 1, 1, 3, 3, 5, 6, 7, 8, 9, 7, 7, 7, 7, 10], k=2))
