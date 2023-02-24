import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    num, segment = map(int,input().split())
    start = 0
    Min = float('inf')
    Max = -1

    li = list(map(int,input().split()))

    for start in range(num-segment+1):
        Sum = 0

        for i in range(start, start+segment):
            Sum += li[i]

        if Min > Sum :
            Min = Sum

        if Max < Sum :
            Max = Sum


    print(f'#{test_case} {Max-Min}')






