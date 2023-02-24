N, M, V = map(int, input().split())
dfslist = []
bfslist = []

def dfs():
    visited = [False for _ in range(N+1)]
    to_visits = [V]
    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            dfslist.append(current)
            visited[current] = True
            to_visits += graph[current]
    return print(*dfslist)


def bfs():
    visited = [False for _ in range(N + 1)]
    to_visits = [V]
    while to_visits:
        current = to_visits.pop(0)
        if not visited[current]:
            bfslist.append(current)
            visited[current] = True
            to_visits += graph[current]
    return print(*bfslist)


graph = [[]for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(1, N+1):
    sorted(graph[i])
dfs()
bfs()
