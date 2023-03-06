from itertools import product


def solution(numbers, target):
    answer = 0
    l = list(product([0, 1], repeat=len(numbers)))

    for row in product([0, 1], repeat=len(numbers)):
        total = 0
        for i in range(len(numbers)):
            total += numbers[i] * -1 if row[i] == 0 else numbers[i]
        if total == target:
            answer += 1

    return answer
