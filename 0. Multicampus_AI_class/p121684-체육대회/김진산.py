from itertools import permutations
def solution(ability):
    answer = 0
    sv_p = 0
    for i in permutations(ability, len(ability[0])):
        point = 0
        for idx, j in enumerate(i):
            point += j[idx]
            if sv_p < point:
                sv_p = point

    answer = sv_p
    return answer


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))