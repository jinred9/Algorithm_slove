
# 외톨이 알파벳을 찾는문제인데 코드로 나타내면 중복되는 알파벳을 제거하고 알파벳순으로
   # 정렬한뒤 중복되는 알파벳을 찾아서 반환할려고하느코드입니다
def solution(input_string):
    answer = ''    # 초기화하는부분이고이후 변수에 중복되는 문자들을저장하게됩니다

    str_list = [input_string[0]] #연속적으로 나오는 알파벳을 저장하고 초기화합니다
    for i in input_string: # i 변수에저장하고 input_string 순회합니다
        if i != str_list[-1]:  # 한 문자가 연속적으로 나타난 경우 제거 하고
            str_list.append(i)  # star list 에추가합니다

    ans = set(str_list) # 중복되지 않은 문자를 ans라는 객체에 저장 하고
    ans = sorted(ans)  # ans 딕셔너리를 알파벳 순으로 정렬함

    for i in ans:   # ans 중복되지 않은 문자들 알파벳순으저장하고
        cnt = 0
        for j in str_list: #하나씩 순회하는 cnt변수를이용하여 str_list에서 몇번
                           #나오는지 셉니다 str_list는 중복되어 나타나는 횟수를 알수잇습니다
            if i == j:# i변수와 j변수가 같으니 비교 str_list 계산
                cnt += 1 # cnt 를 1씩증가시켜서 알파벳을 셉니다

        if cnt > 1:      # cnt가 1보다 큰경우 추가하여
            answer += i   #중복되는 문자를찾아서 answer에 저장합니다

    if answer == '':  # answer가 여전히 빈 문자열인 경우에는 'N'을 추가합니다.
        answer += 'N'

    return answer      # 중복되는 문자가 없는 경우에는 'N'이 반환됩니다.