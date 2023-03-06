import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        # 방향성이 없는경우 추가
        # graph[end].append(start)

    S, G = map(int, input().split())


    def dfs():
        # DFS
        # 방문 여부
        visited = [False for _ in range(V + 1)]
        # 목적지
        to_visits = [S]
        while to_visits:
            # 현재 위치 = 목적지의 마지막
            current = to_visits.pop()
            # 현재 위치를 방문한 적이 없다면
            if not visited[current]:
                print(current)
                # 현재 위치 방문 체크
                visited[current] = True
                # 현재 위치에서 갈 수 있는 정점들을 목적지에 추가
                to_visits += graph[current]

        print(f'#{test_case} {int(visited[G])}')

    def bfs():
        from collections import deque

        # BFS
        # 방문 여부
        visited = [False for _ in range(V + 1)]
        # 목적지
        to_visits = deque()
        to_visits.append(S)
        while to_visits:
            # 현재 위치 = 목적지의 마지막
            current = to_visits.popleft()
            # 현재 위치를 방문한 적이 없다면
            if not visited[current]:
                print(current)
                # 현재 위치 방문 체크
                visited[current] = True
                # 현재 위치에서 갈 수 있는 정점들을 목적지에 추가
                to_visits += graph[current]

        print(f'#{test_case} {int(visited[G])}')
    print('dfs')
    dfs()
    print('bfs')
    bfs()

