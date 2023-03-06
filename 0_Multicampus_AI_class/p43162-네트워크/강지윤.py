def solution(n, computers):
    connected = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    count = 0
    # 영역별로 숫자를 주기 위해
    def dfs(node):
        connected[node] = count

        #영역 별 숫자 부여
        if not visited[node]:
            visited[node] = True
            for col in range(n):
                if node == col:
                    continue
                #자기자신은 제외
                if computers[node][col] == 1:
                    dfs(col)
                #연결되어 있을 경우 탐색 계속

    for i in range(n):
        #전 노드별로 탐색 시작
        if not visited[i]:
            dfs(i)
        unique_connected = set(connected)
        count += 1

    return(len(unique_connected))


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

