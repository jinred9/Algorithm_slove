def solution(input_string):
    answer = ''

    # 외톨이 알파벳으로 의심되는 알파벳만 남기기
    input_string_list = list(input_string[0])  # 리스트 새로 생성

    for alphabet in input_string:
        if alphabet != input_string_list[-1]:  # 생성한 리스트 매개변수로 전달된 문자열과
            input_string_list.append(alphabet) # 비교하며 연속으로 중복된 알파벳 없으면
                                               # 리스트에 추가

    # input_string_list에 남아있는 2개 이상의 외톨이 알파벳을 찾기 위해 중복제거와 알파벳 순으로 분류 후 리스트와 비교할 또 다른 리스트 생성
    string_to_compare = sorted(set(input_string_list))

    for char in string_to_compare:
        count = 0
        for element in input_string_list:
            if char == element:
                count += 1
        if count > 1:  # input_string_list에 한 알파벳이 2개 이상 있을 때 answer에 추가
            answer += char

    if answer == '':  # answer가 그대로 비어있다면 'N' 추가
        answer += 'N'

    return answer