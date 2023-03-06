import sys

sys.stdin = open('input.txt')

T = int(input())
#테스트 케이스 수

for test_case in range(T) :
    problem  = input()
    problem = problem.replace('()','r')
    pipe_num = 0
    result = 0
    for char in problem :
        if char == '(': # 파이프 추가
            pipe_num += 1
        elif char == ')': # : 파이프 끝자리  파이프 갯수 감소 result+=1
            pipe_num -= 1
            result += 1
        else:
            # raser일 경우
            result += pipe_num

    print(result)