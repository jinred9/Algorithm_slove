def solution(n, wires):
    answer = -1
    check_link = [[True]*(n+1) for _ in range(n+1)]
    cnt = 1
    def dfs(v, adj, visited, check_link):
        nonlocal cnt
        # 현재 노드를 방문처리
        visited[v] = True
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in adj[v]:
            if not visited[i] and check_link[v][i]:  # 방문하지 않은 노드인 경우
                cnt += dfs(i, adj, visited, check_link)
        return cnt


    adj = [[] for _ in range(n + 1)]
    for s, e in wires:
        adj[s].append(e)
        adj[e].append(s)
    for s, e in wires:
        visited = [False] * (n + 1)

        check_link[s][e] = False
        cnt_s = dfs(s, adj, visited, check_link)
        cnt_e = dfs(e, adj, visited, check_link)
        check_link[s][e] = True

        answer = min(answer, abs(cnt_s - cnt_e))


    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))