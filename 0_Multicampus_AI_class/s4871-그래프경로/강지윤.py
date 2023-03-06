import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):

    Vertex, Edge = map(int,input().split())

    graph = {}

    for i in range(Edge):
        Start, Arrive = map(int,input().split())

        if Start not in graph:
            graph[Start] = []
            graph[Start].append(Arrive)
        else:
            graph[Start].append(Arrive)

    S, G = map(int,input().split())

    #////////////////// 여기까지 문제 입력받기 ,노드와 간선들 다 받음


    visited = [S]
    #방문 여부
    flag = 0
    #판단
    def dfs(V,G):
        if V == G:
            global flag
            flag = 1
            return

        if V in graph:
            for next_v in graph[V]:
                if next_v not in visited:
                    #만약 방문 되어 있지 않다면
                    visited.append(next_v)
                    dfs(next_v,G)

    dfs(S, G)
    if flag == 1:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')

















