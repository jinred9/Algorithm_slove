from itertools import permutations


def solution(ability):
    answer = 0

    for row in permutations(ability, len(ability[0])):
        s = 0
        for j in range(len(row)):
            s += row[j][j]
        answer = max(answer, s)

    return answer
