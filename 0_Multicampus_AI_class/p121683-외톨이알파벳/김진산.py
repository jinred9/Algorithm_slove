def solution(input_string):
    answer = ''
    solo_alphabet = []
    check_list = []
    temp = []
    for i in input_string:  # input_string을 check_list에 list 형식으로 append
        check_list.append(i)
    for i in range(0, len(check_list)-1):   # idx 범위를 벗어나지 않기 위해 전체 리스트 보다 한개 작게 반복
        if check_list[i] != check_list[i + 1]:  # check_list의 i번째와 i + 1 번쨰가 같지 않은지 확인
            for j in range(i + 1, len(check_list)):     # 같지 않다면 반복해서 i + 1 번부터 반복
                if check_list[i] == check_list[j]:  # i번째와 i + 1 (j)번째가 같은지 반복 체크
                    solo_alphabet.append(check_list[i])     # 같다면 solo_alphabet 리스트에 append

    if len(solo_alphabet) == 0:     # solo_alphabet이 길이가 0 이면 N 출력
        answer = 'N'
        return answer
    else:                           # 아니면 solo_alphabet에 있는 중복 값들을 정렬해서 temp에 삽입
        temp = list(sorted(set(solo_alphabet)))
        answer = ''.join(temp)
        return answer

print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))