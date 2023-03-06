def solution(input_string):
    answer = ''
    # 처음 문자를 last 에 할당
    last = input_string[0]
    # 등장 여부
    appears = [last]

    # 두번째 문자부터 순회
    for current in input_string[1:]:
        # 연속 되면 바로 다음 문자열 보면 됨
        if current == last:
            continue
        else:
            # 기존에 등장한 적 있음(두번째 이상 등장) and 아직 답에는 없음 => 답에 추가
            if current in appears and current not in answer:
                answer += current
            # appears 에 없다면 답에는 당연히 존재할 수 없음 (외톨이의 조건이 2번이상 등장이기 때문)
            else:
                appears.append(current)

            # 마지막 문자열을 현재 문자열로 교체
            last = current

    return ''.join(sorted(answer)) if answer else 'N'


# 'de'
print(solution("edeaaabbccd"))

# 'e'
print(solution("eeddee"))

# 'N'
print(solution("string"))

# 'bz'
print(solution("zbzbz"))
