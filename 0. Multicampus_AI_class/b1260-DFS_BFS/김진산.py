from collections import deque

N, M, V = map(int, input().split())

visited = [False for _ in range(10001)]
graph = [[] for _ in range(N + 1)]
to_visits = [V]
# dfs
for _ in range(M):
    s_point, e_point = map(int, input().split())
    graph[s_point].append(e_point)

while to_visits:
    print(to_visits)
    current = to_visits.pop()

    if not visited[current]:
        print(current, end=' ')
        visited[current] = True
        to_visits += graph[current]

# bfs
for _ in range(M):
    s_point, e_point = map(int, input().split())
    graph[s_point].append(e_point)

to_visits = deque()
to_visits.append(V)
while to_visits:
    current = to_visits.popleft()

    if not visited[current]:
        print(current, end=' ')
        visited[current] = True
        to_visits += graph[current]









