def solution(n, computers):
    # 네트워크는 최소 한개 이상이므로 초기값 1로 설정한다.
    answer = 1
    # 방문기록을 위해 visited를 False로 초기화 한다.
    visited = [False] * n
    # 출발지점을 정해준다.
    to_visits = [0]
    # 다음 갈 곳이 있다면 작동하라
    while to_visits:
        # 현재 갈 곳을 정한다.
        current = to_visits.pop()
        # visited에 현재 방문할 곳을 방문 등록한다.
        if not visited[current]:
            visited[current] = True
            # 현재 컴퓨터와 연결된 노드의 번호를 모든 컴퓨터의 번호를 to_visit에 등록해준다.
            for j in range(n):
                if computers[current][j] == 1 and visited[j] == False:
                    to_visits.append(j)
        # 방문등록 안된 곳이 있으나, 가야할 곳이 없다면 네트워크가 분리되어 있는 것이므로 네트워크(answer) 1증가 한다.
        if False in visited and to_visits == []:
            answer += 1
            count = 0
            # 다음 방문지를 visited의 index가 가장 작은 값으로 할당하여 다시 while문이 작동하도록 to_visits에 값을 할당한다.
            for idx in range(n):
                if visited[idx] == False and count == 0:
                    count += 1
                    to_visits = [idx]
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
