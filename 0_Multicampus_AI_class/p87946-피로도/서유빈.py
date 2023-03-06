from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0

        for required, spent in p:
            if tmp >= required:
                tmp -= spent
                cnt += 1
        answer = max(answer, cnt) # if cnt >= answer, then answer = cnt
    return answer