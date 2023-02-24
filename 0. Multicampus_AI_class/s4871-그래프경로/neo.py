import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 빈 인접 리스트 그래프 생성
    graph = [[] for _ in range(V+1)]

    # 간선 입력
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        # 양방향(무향)그래프 일 경우 아래 줄 추가
        graph[end].append(start)
    S, G = map(int, input().split())
    print("s", S , G)
    print(graph)


    def dfs():
        # S => G 로 갈 수 있는가?
        # DFS
        # 방문 여부
        visited = [False for _ in range(V+1)]
        # 목적지
        to_visits = [S]

        while to_visits:
            # 현재 위치 = 목적지들에서 마지막
            current = to_visits.pop()
            # 현재 위치를 방문한 적이 없다면,
            if not visited[current]:
                print(current)
                # 현재 위치 방문 체크
                visited[current] = True
                # 현재 위치에서 갈 수 있는 정점들을 목적지들에 추가
                to_visits += graph[current]
    dfs()


    # def bfs():
    #     from collections import deque
    #
    #     # 방문 여부
    #     visited = [False for _ in range(V + 1)]
    #     # 목적지
    #     to_visits = deque()
    #     to_visits.append(S)
    #
    #     while to_visits:
    #         # 현재 위치 = 목적지들에서 마지막
    #         current = to_visits.popleft()
    #         # 현재 위치를 방문한 적이 없다면,
    #         if not visited[current]:
    #             print(current)
    #             # 현재 위치 방문 체크
    #             visited[current] = True
    #             # 현재 위치에서 갈 수 있는 정점들을 목적지들에 추가
    #             to_visits += graph[current]
    #
    # bfs()

