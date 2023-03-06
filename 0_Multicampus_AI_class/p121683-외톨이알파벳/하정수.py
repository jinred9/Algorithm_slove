def solution(input_string):
    first = []   # 처음 나온 알파벳 저장 리스트(확인 겸용)
    lone = []   # 두 번 나와서 외톨이가 된 알파벳 리스트
    now = -1   # 리스트 인덱싱을 위해 -1로 초기화
    for char in input_string:
        if now == -1:   # 첫 알파벳은
            first.append(char)   # first리스트에 저장하고
            now += 1   # 현재 인덱스 수정
        else:
            if char not in first:   # 처음나온 알파벳이면
                first.append(char)   # first리스트에 저장하고
                now += 1   # 현재 인덱스 수정
            else:
                if char != first[now]:   # 처음 나온 알파벳이 아닌경우 이전 알파벳과 다를 때
                    first.append(char)   # 현재 알파벳을 first리스트에 저장하고(다음과 현재가 같은지 확인하기 위해)
                    now += 1   # 현재 인덱스 수정
                    lone.append(char)   # 외톨이 알파벳에 추가
# sort 후 set을 하여 계산 시 pycharm에서는 정상작동하지만 제출시 순서가 바뀌지 않음
    cal = []   # 계산용 리스트를 초기화
    for char in set(lone):   # set한 외톨이 알파벳을
        cal.append(char)   # 계산리스트에 추가하고
    cal.sort()   # sort하여 순서를 정렬한다

    answer = ""   # answer에 저장한다
    for char in cal:
        answer += char

    if lone:   # 외톨이알파벳이 있으면 저장한 값을 반환하고
        return answer
    else:   # 없으면 "N"을 추가하여 반환한다
        answer = "N"
        return answer


print(solution("edeaaabbccd"))
