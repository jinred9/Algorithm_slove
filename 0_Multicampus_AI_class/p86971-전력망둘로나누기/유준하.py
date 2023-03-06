from collections import deque
def solution(n, wires):
    result = 0
    graph = [[]for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    def dfs(start):
        visited = [False] * (n + 1)
        to_visits = [start]
        count = 1
        while to_visits:
            current = to_visits.pop()
            if not visited[current]:
                count += 1
                visited[current] = True
                to_visits += graph[current]
        return count
    result = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        result = min(abs(dfs(a) - dfs(b)), result)
        graph[a].append(b)
        graph[b].append(a)
    return result

solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])