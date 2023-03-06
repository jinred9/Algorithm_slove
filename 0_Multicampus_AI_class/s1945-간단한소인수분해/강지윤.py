import sys

sys.stdin = open('input.txt')

T = int(input())
#테스트 케이스 수

kinda = [2,3,5,7,11]
answer = [0,0,0,0,0]

for TestCase in range(T):
    N = int(input())
    #문제에서 주어진수
    while(True):
        if N%kinda[0] == 0:
            N/=kinda[0]
            answer[0]+=1
        elif N%kinda[1] == 0:
            N/=kinda[1]
            answer[1] += 1
        elif N%kinda[2] == 0:
            N/=kinda[2]
            answer[2] += 1
        elif N%kinda[3] == 0:
            N/=kinda[3]
            answer[3] += 1
        elif N%kinda[4] == 0:
            N/=kinda[4]
            answer[4] += 1
        else:
            break

    print(f'#{TestCase+1} {answer[0]} {answer[1]} {answer[2]} {answer[3]} {answer[4]}')
    answer = [0,0,0,0,0]