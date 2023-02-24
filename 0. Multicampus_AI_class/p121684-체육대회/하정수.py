from itertools import permutations


def solution(ability):
    answer = 0   # 최고점수를 0으로 초기화한다
    for do_players in permutations(ability, len(ability[0])):   # 출전할 선수를 종목 수 만큼 순열로 뽑는다
        total = 0   # 이번 출전선수의 총점을 초기화 한다
        for i in range(len(ability[0])):   # 종목 수만큼
            total += do_players[i][i]   # 자기 차례의 종목의 점수를 더한다
        if total > answer:   # 현 총점이 최고점수보다 높다면
            answer = total   # 입력해준다
    return answer


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))
