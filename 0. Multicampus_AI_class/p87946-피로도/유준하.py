from itertools import permutations
# 순열 함수를 사용해 해결 하는 방법
def solution(k, dungeons):
    answer = -1
    dungeons_kind = list(permutations(dungeons, len(dungeons)))
    for dlist in dungeons_kind:
        check = 0
        energy = k
        for dcal in dlist:
            if energy >= dcal[0] and energy > 0:
                energy -= dcal[1]
                check += 1
        if check >= answer:
            answer = check
    return answer

# 재귀를 활

