def solution(s, e):
    # 목적지가 더 뒤에 있다면, 최대한 빨리 가까이 가자
    if s < e:
        count = (e-s) // 5
        s += (count * 5)
    # 목적지가 더 앞에 있다면, 가는 수 밖에
    elif s > e:
        return s - e

    # 몇 번만에 찾았는지
    count = 0
    # 목적지
    to_visits = [s]
    # 방문 여부
    visited = [False for _ in range(10001)]

    while to_visits:
        # 목적지 횟수 만큼 반복
        for _ in range(len(to_visits)):
            # 현재 위치 갱신
            current = to_visits.pop(0)
            #방문한 적 없다면,
            if not visited[current]:
                # 방문 체크
                visited[current] = True
                # 찾았다면, 끝
                if current == e:
                    return count
                # 못 찾았다면, 이동할 수 있는 선택지들
                for nxt in [current-1, current+1, current+5]:
                    # 선택지들이 범위 안이고, 방문한 적 없다면,
                    if 0 < nxt <= 10000 and not visited[nxt]:
                        to_visits.append(nxt)

        count += 1
    return count



# 3
print(solution(5, 14))
# 5
print(solution(8, 3))