def solution(input_string):
    current_string = None
    history = []
    input_string += ' '
    #이미 한번 기록된 것
    Nerd = []
    #외톨이 단어
    Len = 0
    #연속된 단어의 갯수를 의미한다.
    #개요 : 루프를 돌면서 같은 문자가 연속으로 나오면 continue 다른 문자가 나올경우 Len 비교
    for c in input_string:
        if not current_string:
            current_string = c
            Len = 1
            continue
        #맨 처음 current_string이 없을 떄

        if current_string == c :
            Len += 1
        else:
            if current_string not in history:
                history.append(current_string)
            else:
                history.append(current_string)
                Nerd.append(current_string)

            current_string = c

    Nerd = set(Nerd)
    Nerd = list(Nerd)
    Nerd.sort()

    if not Nerd:
        return 'N'
    else:
        sum_string = ''
        for c in Nerd:
            sum_string += c
        return sum_string










print(solution("edeaaabbccd"))
print(solution('string'))
print(solution('zbzbz'))
print(solution("eeddee"))