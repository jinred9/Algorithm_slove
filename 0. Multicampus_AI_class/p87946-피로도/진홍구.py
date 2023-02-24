# ====================================================================
#  DFS 풀이















# ====================================================================
#  순열조합 풀이
from itertools import permutations

def solution1(k, dungeons):
    answer = -1
    # 순열함수로 모든 순열 조합에 대해 list 생성
    nPr = list(permutations(dungeons, len(dungeons)))
    # 각 순열조합에 대한 던전을 clear한 경우 초기화
    clear_dungeons = [0]
    # for 문으로 각 순열조합에 대한 던전 입장
    for nPr_item in nPr:
        # 던전을 clear한 경우 초기화
        count = 0
        # 각 순열 조합에 대해 던전 입장시에 피로도 초기화
        k_current = k
        # 던전입장
        for nPr_item_each in nPr_item:
            if nPr_item_each[0] <= k_current:
                k_current -= nPr_item_each[1]
                count += 1
        clear_dungeons.append(count)
    answer = max(clear_dungeons)
    return answer


k = 40
dungeons = [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]
print(solution1(k, dungeons))
# answer = 4
k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution1(k, dungeons))
# answer = 3

# ======================================================================

