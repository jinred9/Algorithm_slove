import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(input()) #구분자가 없는 문자열의 경우 list로 변환시 문자열 하나씩 요소로 저장
    dict = {}
    max = 0

    for i in num:
        if i in dict: #key로 value 찾기 (dict.get(i)도 가능)
            dict[i] += 1
        else:
            dict[i] = 1


    for k, v in dict.items():
        if v > max:
            max = v
            ans = [k,v]
    print( f'#{tc} {ans[0]} {ans[1]}')
