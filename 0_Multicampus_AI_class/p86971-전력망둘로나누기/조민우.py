def solution(n, wires):
    # 빈 인접 리스트 그래프 생성
    answer = []
    graph = [[] for _ in range(n + 1)]
    node_status = [[True]*(n+1) for _ in range(n + 1)]

    # 간선 입력
    for E in wires:
        start, end = E
        graph[start].append(end)
        # 양방향(무향)그래프 일 경우 아래 줄 추가
        graph[end].append(start)
    def dfs(v):
        count = 1
        visited[v] = True
        for new_v in graph[v]:
            if not visited[new_v] and node_status[v][new_v]:
                count += dfs(new_v)
        return count

    for vertices in wires:
        visited = [False for _ in range(n + 1)]
        start_d, end_d = vertices
        node_status[start_d][end_d] = False
        div_a = dfs(start_d)
        div_b = dfs(end_d)
        node_status[start_d][end_d] = True
        answer.append(abs(div_a - div_b))
    return min(answer)

