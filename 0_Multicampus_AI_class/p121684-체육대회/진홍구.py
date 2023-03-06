
# # code by 하정수 =======================================================================
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


# # code by 유준하 =======================================================================
# from itertools import combinations, permutations
# def solution(ability):
#     answer = 0
#     student = list(permutations(ability, len(ability[0])))
#     for slist in student:
#         ab = 0
#         for i in range(0, len(ability[0])):
#             ab += slist[i][i]
#         if answer < ab:
#             answer = ab
#     return answer
#
# print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
# print(solution([[20, 30], [30, 20], [20, 30]]))


# # code by 하정수 =======================================================================
# from itertools import combinations, permutations
# def solution(ability):
#     answer = 0   # 최고점수를 0으로 초기화한다
#     for do_players in permutations(ability, len(ability[0])):   # 출전할 선수를 종목 수 만큼 순열로 뽑는다
#         total = 0   # 이번 출전선수의 총점을 초기화 한다
#         for i in range(len(ability[0])):   # 종목 수만큼
#             total += do_players[i][i]   # 자기 차례의 종목의 점수를 더한다
#         if total > answer:   # 현 총점이 최고점수보다 높다면
#             answer = total   # 입력해준다
#     return answer
#
# print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
# print(solution([[20, 30], [30, 20], [20, 30]]))



