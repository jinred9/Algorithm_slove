

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs():
    # S => G 로 갈 수 있는가?
    # DFS
    # 방문 여부
    visited = [False for _ in range(N + 1)]
    # 목적지
    to_visits = [V]
    while to_visits:
        # 현재 위치 = 목적지들에서 마지막
        current = to_visits.pop()
        # 현재 위치를 방문한 적이 없다면,
        graph[current].sort()
        graph[current].reverse()
        if not visited[current]:
            print(current)
            # 현재 위치 방문 체크
            visited[current] = True
            # 현재 위치에서 갈 수 있는 정점들을 목적지들에 추가
            to_visits += graph[current]

            # to_visits.sort()
dfs()


def bfs():
    from collections import deque

    # 방문 여부
    visited = [False for _ in range(N + 1)]
    # 목적지
    to_visits = deque()
    to_visits.append(V)

    while to_visits:
        # 현재 위치 = 목적지들에서 마지막
        current = to_visits.popleft()
        # 현재 위치를 방문한 적이 없다면,
        graph[current].sort()
        if not visited[current]:
            print(current)
            # 현재 위치 방문 체크
            visited[current] = True
            # 현재 위치에서 갈 수 있는 정점들을 목적지들에 추가
            to_visits += graph[current]
bfs()