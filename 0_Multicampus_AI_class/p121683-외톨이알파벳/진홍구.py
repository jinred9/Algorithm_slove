def solution(input_string):
    # 출력값 초기화
    answer = ''
    # 입력값 list로 만들기
    letter_lists = list(input_string)
    # 출력값이 오름차순이어야 하므로, set -> 오름차순으로 정렬함
    letter_list_only = sorted(set(letter_lists))

    for letter in letter_list_only:
        solo_letter = 0
        for i in range(0, len(letter_lists)):
            if letter == letter_lists[i] and solo_letter == 0:
                for j in range(i + 1, len(letter_lists)):
                    if letter != letter_lists[j] and solo_letter == 0:
                        for k in range(j + 1, len(letter_lists)):
                            if letter == letter_lists[k] and solo_letter == 0:
                                solo_letter += 1
                                answer += letter
    if answer == '':
        answer ='N'
    return answer





input_string = "edeaaabbccd"
print(solution(input_string))
# answer : 'de'
input_string = "eeddee"
print(solution(input_string))
# answer : 'e'
input_string = "string"
print(solution(input_string))
# answer : 'N'
input_string = "zbzbz"
print(solution(input_string))
# answer : 'bz'
