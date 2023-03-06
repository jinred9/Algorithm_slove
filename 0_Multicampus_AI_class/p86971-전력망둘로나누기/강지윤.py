# 점진적으로 노드를 탐색하면서 전체 갯수로 부터 빼나간다.

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for Edge in wires:
        start, End = Edge
        graph[start].append(End)
        graph[End].append(start)
    answer = []
    count = 0

    def dfs(Node):
        nonlocal count
        if not visited[Node]:
            visited[Node] = True
            count += 1
            for Next_Node in graph[Node]:
                if Next_Node == Node:
                    continue
                dfs(Next_Node)
            visited[Node] = False

    #엣지를 하나씩 빼가면서 브루트포스로 dfs로 짠다.
    for Edge in wires:
        start, End = Edge
        graph[start].remove(End)
        graph[End].remove(start)
        for node in graph:
            if node :
                dfs(node[0])
                break
            #그래프 중에 안비어있는 곳을 찾고 그 노드를 기준으로 dfs를 돌아라
        count2 = n - count
        answer.append(abs(count2-count))
        count = 0
        graph[start].append(End)
        graph[End].append(start)

    return min(answer)



print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))