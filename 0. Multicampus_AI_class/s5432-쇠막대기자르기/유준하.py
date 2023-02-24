import sys

sys.stdin = open('input.txt')


testcase = int(input())
for i in range(1, testcase+1):
    arrange = input()
    pipe = []
    result = 0
    razer = []
    arrange = arrange.replace('()', 'r')  # 문자열 for문 loop 돌 때 레이저임을 판별하기 위해 ()를 r로 치환
    for cuts in range(0, len(arrange)):
        if arrange[cuts] == '(':         # 열린 괄호이면 STACK에 1 저장
            pipe.append(1)
        elif arrange[cuts] == ')':       # 닫힌 괄호이면 pop 하면서 마지막 값 result에 누적
            result += pipe.pop(-1)
        else:
            razer.append(sum(pipe))     # 레이저 이면 pipe의 갯수 저장
    print(f"#{i} {result+sum(razer)}")
    print(result)


# 닫힌 괄호의 수 + 레이저의 수 = 절단된 쇠파이프의 갯수
# stack을 활용해 정상적인 괄호 찾기 문제와 유사함
