from itertools import permutations

def solution(ability):
    answer = 0
    student = list(permutations(ability, len(ability[0])))
    for slist in student:
        ab = 0
        for i in range(0, len(ability[0])):
            ab += slist[i][i]
        if answer < ab:
            answer = ab
    return answer