def solution(gems):
    minimum = N = len(gems)
    gemInfo = {}
    start = 0
    findOfGems = len(set(gems))
    answer = [1,N]
    for end in range(N):
        last_gem = gems[end]
        if gemInfo.get(last_gem):
            gemInfo[last_gem] += 1
        else :
            gemInfo[last_gem] = 1
        # 젬이 있으면 1을 더해주고 없으면 다시 키 밸류 값을 생성

        while(len(gemInfo) == findOfGems):

            numOfGems = end - start + 1

            if minimum > numOfGems:
                minimum = numOfGems
                answer = [start + 1 , end+ 1]

            start_gem = gems[start]

            gemInfo[start_gem] -= 1

            if gemInfo[start_gem] == 0:
                gemInfo.pop(start_gem)

            start += 1


    return answer

























print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

print(solution(["AA", "AB", "AC", "AA", "AC"]))

print(solution(["XYZ", "XYZ", "XYZ"]))

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))