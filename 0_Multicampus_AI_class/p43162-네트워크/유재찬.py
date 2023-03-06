def check(computers, visited, idx):
    visited[idx] = True
    s = [idx]
    while s:
        curr_idx = s.pop()
        for next_idx, val in enumerate(computers[curr_idx]):
            if val == 1 and visited[next_idx] is False:
                visited[next_idx] = True
                s.append(next_idx)
    return True


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] is False:
            answer += check(computers, visited, i)
    return answer
