def solution(input_string):
    element = list(set(input_string))
    element_part = {}
    answer = []

    # 해당 요소가 외톨이인지 검사(요소 만큼 for문)
    for i in element:
        idx = 0
        if 2 <= input_string.count(i):
            while idx < len(input_string):
                idx = input_string.find(i, idx)
                if idx == -1:
                    break
                if i not in element_part:
                    element_part[i] = []
                    element_part[i].append(idx)
                else:
                    element_part[i].append(idx)
                idx += 1
            # 외톨이 조건 중 2개 이상 부분에 나눠져 있는 경우,
            lst = element_part[i]
            for idx in range(len(lst) - 1):
                if lst[idx + 1] - lst[idx] > 1:
                    answer.append(i)
                    break

    answer.sort()
    if answer:
        return ''.join(answer)
    else:
        return 'N'


print(solution("edeaaabbccd"))  # de
print(solution("eeddee"))       # e
print(solution("string"))       # N
print(solution("zbzbz"))        # bz
