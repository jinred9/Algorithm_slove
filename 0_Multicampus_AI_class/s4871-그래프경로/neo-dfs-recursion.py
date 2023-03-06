import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 빈 인접 리스트 그래프 생성
    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    # 간선 입력
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        # 양방향(무향)그래프 일 경우 아래 줄 추가
        graph[end].append(start)
    S, G = map(int, input().split())

    print(graph)

    def dfs(v):
        visited[v] = True
        for new_v in graph[v]:
            if not visited[new_v]:
                dfs(new_v)

    dfs(S)
