import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    N, M = map(int,input().split())
    total = []
    sum = 0
    graph = [list(map(int, input().split())) for i in range(N)]


    for r in range(N-M+1):
        for c in range(N-M+1):
            for r_M in range(r,r+M):
                for c_M in range(c,c+M):
                    sum += graph[r_M][c_M]

            total.append(sum)
            sum = 0

    print(f'#{test_case} {max(total)}')









