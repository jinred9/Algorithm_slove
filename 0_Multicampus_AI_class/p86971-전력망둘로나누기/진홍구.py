def solution(n, wires):
    answer = -1

    graph = [[] for _ in range(n + 1)]
    # Graph작성
    for i in range(len(wires)):
        start, end = wires[i]
        graph[start].append(end)
        graph[end].append(start)
    for i in range(len(graph)):
        graph[i] = sorted(graph[i], reverse=True)
    def dfs_def(n, start, block, graph):
        # 방문한 정점 초기화
        visited = [False for _ in range(n + 1)]
        # 선로 자르는 것을 상태편 송전탑을 True로 만들어 network가 연결 안되도록 함.
        visited[block] = True
        # 현재 위치에 시작정점 할당
        current = start
        # 방문한 정점 초기화
        to_visits = [current]
        count = 0
        while to_visits:
            current = to_visits.pop()
            if not visited[current]:
                count += 1
                visited[current] = True
                to_visits += graph[current]
        return abs(n - (count * 2))
    diff_arr = []
    for i in range(1, n+1):
        for j in graph[i]:
            diff_arr.append(dfs_def(n, i, j, graph))
    answer = min(diff_arr)

    return answer







print(solution(2, [[1,2]]))
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))