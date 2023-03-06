def solution(ability):
    answer = 0   # 최고 총점
    is_done = [False] * len(ability)   # 이미 출전한 선수들 확인

# 출전하는 선수 조합을 검색
    def search(idx, total):
        nonlocal answer

        if idx == len(ability[0]):   # 출전한 선수가 종목수와 같다면
            if answer < total:   # 총점이 최고 총점보다 크다면
                answer = total   # 값을 저장한 후
            return   # 함수를 종료한다

        for player in range(len(ability)):   # 출전 가능한 선수들 중에
            if not is_done[player]:   # 아직 출전하지 않은 경우
                total += ability[player][idx]   # 총점에 현재 순서 경기값을 더해주고
                is_done[player] = True   # 출전한 선수로 바꾸어준 후
                search(idx+1, total)   # 다음 경기 선수를 골라준다
                is_done[player] = False   # 현재 선수를 출전시키지 않고
                total -= ability[player][idx]   # 현재 선수의 점수를 빼준다

    search(0, 0)
    return answer


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
