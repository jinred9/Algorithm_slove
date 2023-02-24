import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    N = int(input())

    graph = [[0]*N for _ in range(N)]

    if N == 1:
        print(f'#{test_case}')
        print(1)

    elif N == 2 :
        print(f'#{test_case}')
        print(1)
        print(1,1)

    else:
        graph[0][0] = 1
        graph[1][0] = graph[1][1] = 1

        for i in range(N):
            graph[i][0] = graph[i][i] = 1



        for floor in range(2,N): #floor+1이 층수
            for e in range(1,floor):
                graph[floor][e] = graph[floor-1][e-1] + graph[floor-1][e]


        print(f'#{test_case}')
        for row in range(N):
            for col in range(N):
                if graph[row][col]:
                    print(graph[row][col], end=' ')

            print()





















