def solution(gems):
    answer = []
    temp = list(set(gems))
    low_gem = 0
    high_gem = len(gems)
    mid_gem = (low_gem + high_gem) // 2

    for i in range(gems):

        if gems[mid_gem] == temp:
            answer += mid_gem
        elif gems[mid_gem] > temp:
            mid_gem -= 1
        else:
            mid_gem += 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

def solution(gems):
    start = 0
    N = minimum = len(gems)
    uniq_count = len(set(gems))
    answer = [1, N+1]
    # 구매 내역
    gem_info = {}
    for end in range(N):
        last_gem = gems[end]
        # 구매했다면 + 1
        if gem_info.get(last_gem):
            gem_info[last_gem] += 1
        # 처음이라면 추가
        else:
            gem_info[last_gem] = 1

        # 모두 샀다면,
        while uniq_count == len(gem_info):
            # 현재 산 보석 개수
            count = end - start + 1
            if count < minimum:
                minimum = count
                answer = [start + 1, end]

            first_gem = gems[start]
            gem_info[first_gem] -= 1

            if gem_info[first_gem] == 0:
                gem_info.pop(first_gem)

            start += 1
    return answer

