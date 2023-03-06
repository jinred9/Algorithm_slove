def get_count(adjust, visited, start_idx):
    visited[start_idx] = True
    s = [start_idx]
    cnt = 0
    while s:
        curr_idx = s.pop()
        cnt += 1
        for next_idx in adjust[curr_idx]:
            if visited[next_idx] is False:
                visited[next_idx] = True
                s.append(next_idx)
    return cnt


def solution(n, wires):
    answer = float('inf')
    for excluded_adj in range(len(wires)):
        ADJUST = [[] for _ in range(n + 1)]
        for i, (v1, v2) in enumerate(wires):
            if i == excluded_adj:
                continue
            ADJUST[v1].append(v2)
            ADJUST[v2].append(v1)

        visited = [False for _i in range(n + 1)]

        counts = []
        for idx in range(1, n + 1):
            if visited[idx] is False:
                cnt = get_count(ADJUST, visited, idx)
                counts.append(cnt)

        answer = min(abs(counts[0] - counts[1]), answer)

    return answer
