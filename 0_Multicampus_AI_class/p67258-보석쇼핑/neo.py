# O(2n)
def solution(gems):
    start = 0
    N = minimum = len(gems)
    uniq_count = len(set(gems))
    answer = [1, N]
    # 구매 내역
    gem_info = {}

    for end in range(N):
        last_gem = gems[end]
        # 구매했다면 +1
        if gem_info.get(last_gem):
            gem_info[last_gem] += 1
        # 처음이라면 추가
        else:
            gem_info[last_gem] = 1

        # 모두 샀다면,
        while uniq_count == len(gem_info):
            # 현재 산 보석 개수
            count = end - start + 1
            # 현재 산 개수가 지금까지 산것보다 작으면
            if count < minimum:
                # 최소값 갱신
                minimum = count
                # 현재 기록
                answer = [start+1, end+1]

            first_gem = gems[start]
            gem_info[first_gem] -= 1
            # 구매 내역에서 0개가 되면 dict에서 삭제
            if gem_info[first_gem] == 0:
                # 구매 리스트에서 삭제 (pop이 실행될 경우 while 탈출 => end 전진하러 감)
                # 만약 end 가 끝까지 갔는데 이 while 문에 들어 오지 못할 경우, 마지막 구간이 답이 됨.
                gem_info.pop(first_gem)

            start += 1
    return answer


# O(n^2)
# def solution(gems):
#     N = minimum = len(gems)
#     uniq_count = len(set(gems))
#     answer = [1, N]
#     for start in range(0, N-uniq_count+1):
#         for end in range(start+uniq_count, N+1):
#             my_gems = gems[start:end]
#             if len(set(my_gems)) == uniq_count and len(my_gems) < minimum:
#                 minimum = len(my_gems)
#                 answer[0] = start + 1
#                 answer[1] = end
#                 break
#     return answer



# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))