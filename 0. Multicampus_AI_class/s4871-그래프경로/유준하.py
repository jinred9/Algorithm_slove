import sys
sys.stdin = open('input.txt')
testcase = int(input())


def dfs(s, g):
    visited = [False for _ in range(vertex+1)]  # 방문 여부 확인
    to_visits = [s]  # 목적지
    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            to_visits += graph[current]
    return int(visited[g])


def bfs(s, g):
    visited = [False for _ in range(vertex + 1)]  # 방문 여부 확인
    to_visits = [s]  # 목적지
    while to_visits:
        current = to_visits.pop(0)
        if not visited[current]:
            visited[current] = True
            to_visits += graph[current]
    return int(visited[g])


for i in range(1, testcase+1):
    vertex, edge = map(int, input().split())
    graph = [[]for _ in range(vertex+1)]
    for _ in range(edge):
        start, end = map(int, input().split())
        graph[start].append(end)
    S, G = map(int, input().split())
    answer = dfs(S, G)
    print(f"# {i} {answer}")