def solution(s, e):
    to_visited = [s]
    visited = [False for _ in range(10000)]
    count = 0
    while to_visited:
        # 목적지 횟수 만큼 반복
        for _ in range(len(to_visited)):
            current = to_visited.pop(0)
            if not visited[current]:
                visited[current] = True
                if current == e:
                    return count
                for nxt in [current-1, current+1, current+5]:
                    if 0 < nxt <= 10000 and not visited[nxt]:
                        to_visited.append(nxt)
        count += 1
    return count