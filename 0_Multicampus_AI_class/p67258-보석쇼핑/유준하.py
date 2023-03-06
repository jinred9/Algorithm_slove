
def solution(gems):
    start = 0
    N = minimum = len(gems)
    uniq_count = len(set(gems))
    gem_info = {}
    answer = [1, N]
    for end in range(N):
        last_gems = gems[end]
        if gem_info.get(last_gems):
            gem_info[last_gems] += 1
        else:
            gem_info[last_gems] = 1
    #  모두 샀다면,
        while uniq_count == len(gem_info):
        # 현재 산 보석 개수
            count = end - start + 1
            if count < minimum:
                minimum = count
                answer = [start + 1, end+1]

            first_gem = gems[start]
            gem_info[first_gem] -= 1
            if gem_info[first_gem] == 0:
                gem_info.pop(first_gem)
            start += 1
    return answer
