import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    string = list(input())
    answer =[]   #빈 리스트 : false

    for s in string:
        if answer and s == answer[-1]: # 리스트가 비어있지 않고, 끝자리 인덱싱과 s가 같다면
            answer.pop() #리스트에서 제거
        else:
            answer.append(s)  #리스트에 추가

    print(f'#{tc} {len(answer)}') #len함수로 list 요소세기


