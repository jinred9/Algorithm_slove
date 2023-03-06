from itertools import permutations


def solution(k, dungeons):
    answer = -1
    need = []   # 필요치
    spend = []   # 소모치
# 각각 리스트로 저장
    for dungeon in dungeons:
        need.append(dungeon[0])
        spend.append(dungeon[1])
# 던전의 개수만큼 순열 반복
    for perm in permutations(range(len(dungeons))):
        energy = k   # 이번 순열에서 사용하는 에너지 초기화
        done = 0   # 탐험 횟수 초기화
        for i in range(len(perm)):   # 순열의 길이만큼 반복
            if energy >= need[perm[i]]:   # 현재 에너지가 순열에서 탐험하는 던전의 필요치보다 높으면
                energy -= spend[perm[i]]   # 현재 에너지에서 소모치를 빼고
                done += 1   # 탐험횟수를 1 증가시킨다
# 탐험횟수가 answer보다 크면 그 값을 넣어준다
        if done > answer:
            answer = done

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
