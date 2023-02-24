# input_string : 소문자로만 구성된 문자열
# 뭉쳐있지 않는 알파벳 출력

def solution(input_string):
    word = list(input_string)
    sol = []    # 외톨이 알파벳
    for i in range(0, len(input_string)-1):
        if word[i] == word[i+1]:
            pass
        else:
            for j in range(i+1, len(input_string)):
                if word[i] != word[j]:
                    pass
                else:
                    sol.append(word[i])
    if len(sol) == 0:
        answer = 'N'
        return answer
    else:
        ans = list(sorted(set(sol)))
        answer = ''.join(ans)
        return answer
