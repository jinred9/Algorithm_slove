def solution(n, computers):
    answer = 0
    visited = [False] * (n)     # DFS 방문 여부 확인을 위한 visited 리스트

    def dfs(start):
        visited[start] = True    # 시작 지점 start의 방문 상태 True
        for x in range(0, n):    # computers의 시작 지점을 기준으로 인접형렬 내 값 비교를 위한 for 루프
            if computers[start][x] == 1 and not visited[x]:   # 만약 해당 위치가 1 이면서 다음 노드가 방문되지 않았다면 dfs 재귀
                dfs(x)

    for i in range(n):
        if not visited[i]:    # 방문여부 리스트 상태가 False 일 경우 dfs
            dfs(i)
            answer += 1       # 한경로의 끝에 도달할 때 마다 answer += 1
    print(answer)


