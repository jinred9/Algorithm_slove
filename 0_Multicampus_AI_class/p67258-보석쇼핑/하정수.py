def solution(gems):
    start = 0
    n = minimum = len(gems)
    kind = len(set(gems))
    answer = [1, n]
    buy_gems = {}
    for end in range(n):
        last_gem = gems[end]
        if buy_gems.get(last_gem):
            buy_gems[last_gem] += 1
        else:
            buy_gems[last_gem] = 1

        while kind == len(buy_gems):
            count = end - start + 1
            if count < minimum:
                minimum = count
                answer = [start + 1, end + 1]

            first_gem = gems[start]
            buy_gems[first_gem] -= 1

            if buy_gems[first_gem] == 0:
                buy_gems.pop(first_gem)

            start += 1

    return answer




# def solution(gems):
#     every = len(gems)
#     want_gems = list(set(gems))   # 원하는 보석의 리스트를 만든다
#     kind = len(want_gems)   # 원하는 보석의 종류를 저장한다
#     possible = [0, 0, every]   # 가능한 구간과 구간의 길이를 만들고 초기화한다
#     for start in range(every - kind + 1):   # 시작부분은 전체에서 원하는 보석 수만큼 뺀 것 보다 한 번 더 해야한다 ex) 5개중 3개를 원하면 3번까지는 해야한다.
#         test_gems = want_gems[:]   # 원하는 보석이 있으면 제거할 test_gems리스트를 만든다.
#         test_gems.remove(gems[start])   # 첫번째는 반드시 구매하므로 첫 보석을 제거한다
#         for end in range(start, every):   # 마지막 보석까지 test_gems 리스트와 비교 이때 첫보석부터 시작하여 1개인 경우 대비
#             if gems[end] in test_gems:   # 현재 보석이 test_gems 리스트에 있으면 제거
#                 test_gems.remove(gems[end])
#             if len(test_gems) == 0:   # test_gems 리스트에 남은것이 없으면 가능한 구간에 저장
#                 if (end - start) < possible[2]:
#                     possible = [start + 1, end + 1, end - start]
#
#     answer = possible[0:2]
#     return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
