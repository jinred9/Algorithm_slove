def solution(n, computers):
    edges = [0]   # 연결된 컴퓨터의 리스트를 초기화(0을 넣어 인덱스와 맞추어준다)
    is_linked = [False for _ in range(n+1)]   # 네트워크 방문 여부를 False로 초기화한다.
    is_linked[0] = True   # 인덱스를 맞추기 위해 0번을 True로 바꿔준다
    network = 0   # 네트워크의 개수를 0개로 초기화한다
    for i in range(n):   # 모든 컴퓨터 마다
        networks = []   # 연결된 컴퓨터를 저장하기 위한 리스트
        for j in range(n):   # 연결여부 확인
            if computers[i][j] == 1:   # 열이 1이면
                networks.append(j+1)   # 열 + 1을 추가한다(컴퓨터 번호로 맞추기 위해)
                if i == j:   # 만약 자기자신이면
                    networks.pop()   # pop으로 제거한다
        edges.append(networks)   # 연결된 컴퓨터를 리스트에 넣어준다

    for i in range(1, n+1):   # 컴퓨터 수만큼 (컴퓨터 번호로 맞추었으므로 1부터 시작)
        if not is_linked[i]:   # 현재 컴퓨터가 연결되지 않았다면
            network += 1   # 네트워크 수를 1개 늘려준다

        to_visit = edges[i]   # 방문할 곳을 연결된 컴퓨터 리스트에서 가져온다
        is_linked[i] = True   # 해당 컴퓨터를 연결상태로 바꿔준다
        while to_visit:
            now = to_visit.pop()   # 현재 컴퓨터를 방문할 곳에서 pop하고
            if not is_linked[now]:   # pop 한 값이 방문한 적 없다면
                is_linked[now] = True   # 방문했다고 바꾸어주고
                to_visit += edges[now]   # 현재 컴퓨터와 연결된 리스트를 추가한다

    return network


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
