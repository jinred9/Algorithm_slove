def solution(n, wires):
    answer = n   # 정답을 최대길이로 초기화 한다
    for i in range(len(wires)):   # 연결 수 만큼
        test = wires[:]   # 연결 리스트를 복사하고
        test.pop(i)   # i번째 연결을 끊는다
        edges = [[] for _ in range(n + 1)]   # 연결 리스트를 만든다
        linked = 0   # 연결된 수를 0으로 초기화한다
        is_visited = [False] * (n + 1)   # 방문 여부를 초기화한다
        for s, e in test:   # 연결 상황을 리스트에 넣어준다
            edges[s].append(e)
            edges[e].append(s)

        # DFS로 확인하는 함수
        def check(start):
            nonlocal linked   # 연결수를 사용하고
            if not is_visited[start]:   # 방문하지 않았다면
                is_visited[start] = True   # 방문체크하고
                linked += 1   # 연결수를 늘려준다
                for j in edges[start]:   # 현재 송전탑의 연결 리스트만큼
                    check(j)   # 확인을 계속해준다.

        check(1)   # 아무 송전탑이나 하나만 체크해도 된다(전체가 연결되어있다는 가정이므로)
        if answer > abs(n-2*linked):   # 차이의 절댓값이 더 작다면
            answer = abs(n-2*linked)   # 그 값을 넣어준다
    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
