import sys

sys.stdin = open('input.txt')

T = int(input())
#테스트 케이스 수

for test_case in range(1,T+1):
    N, Q = map(int, input().split())
    boxes = [0]*(N+1)
    for i in range(Q):
        L,R = map(int,input().split())
        for N in range(L,R+1):
            boxes[N] = i+1

    boxes = boxes[1:]
    answer = '#'+str(test_case)+' '
    for boxnum in boxes:
        answer = answer+str(boxnum)+' '

    print(answer)








