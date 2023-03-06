import sys

sys.stdin = open('input.txt')


def dfs_bfs_def(N, M, V, graph, k):
    # k == 0 : bfs, k == -1 : dfs
    # 방문한 정점 초기화
    visited = [False for _ in range(N + 1)]
    # 현재 위치에 시작정점 할당
    current = V
    # 방문한 정점 초기화
    visite_order = []
    to_visits = [current]
    while to_visits:
        current = to_visits.pop(k)
        if visited[current]:
            pass
        elif not visited[current]:
            visited[current] = True
            if k == -1:
                graph[current].sort(reverse=True)
            else:
                graph[current].sort()
            to_visits += graph[current]
            visite_order.append(current)
    return visite_order


T = int(input())
for test_case in range(1, T + 1):
    # N : 정점, M : 간선, V : 시작정점
    N, M, V = map(int, input().split())
    # 입력값을 받아 Graph 작성
    # Graph 초기화
    graph_dfs = [[] for _ in range(N + 1)]
    # Graph작성
    for _ in range(M):
        start, end = map(int, input().split())
        graph_dfs[start].append(end)
        graph_dfs[end].append(start)
    graph_bfs = graph_dfs.copy()

    print(*dfs_bfs_def(N, M, V, graph_dfs, -1))
    print(*dfs_bfs_def(N, M, V, graph_bfs, 0))

# def dfs_def(N, M, V, graph):
#     # 방문한 정점 초기화
#     visited = [False for _ in range(N + 1)]
#     # 현재 위치에 시작정점 할당
#     current = V
#     # 방문한 정점 초기화
#     visite_order = []
#     to_visits = [current]
#     while to_visits:
#         current = to_visits.pop()
#         if visited[current]:
#             pass
#         elif not visited[current]:
#             visited[current] = True
#             graph[current].sort(reverse=True)
#             to_visits += graph[current]
#             visite_order.append(current)
#     return visite_order


# def bfs_def(N, M, V, graph):
#     # 방문한 정점 초기화
#     visited = [False for _ in range(N + 1)]
#     # 현재 위치에 시작정점 할당
#     current = V
#     # 방문한 정점 초기화
#     visite_order = []
#     to_visits = [current]
#     while to_visits:
#         current = to_visits.pop(0)
#         if visited[current]:
#             pass
#         elif not visited[current]:
#             visited[current] = True
#             graph[current].sort()
#             to_visits += graph[current]
#             visite_order.append(current)
#     return visite_order
