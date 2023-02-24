import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    fly_map = []  # 파리의 마릿수 정보를 저장할 리스트 생성
    max_kill = 0
    row, attack = map(int, input().split())  # 파리 리스트 크기와 파리채 크기를 저장

    for column in range(row):
        fly_map.append(input().split())  # 파리 마릿수 리스트 저장(정수형으로 받으면 더 좋을 듯 하지만 실패)
        # fly_map.append(list(map(int, input().split())))를 사용하여 정수형으로 저장 가능

    for to_right in range(row - attack + 1):  # 파리채로 공격할 범위의 좌측 상단값 결정
        for to_down in range(row - attack + 1):  # 파리채로 공격할 범위의 좌측 상단값 결정
            kill = 0
            for i in range(to_right, to_right + attack):  # 파리채로 공격한 위치 결정
                for j in range(to_down, to_down + attack):  # 파리채로 공격한 위치 결정
                    kill += int(fly_map[i][j])  # 파리채로 공격한 파리 수 더하기
            if kill > max_kill:
                max_kill = kill  # 최댓값이면 저장해주기
    print(f'#{test_case} {max_kill}')

# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     N_list = [list(map(int, input().split())) for _ in range(N)]
#
#     die_fly = []
#
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             fly = 0
#             for k in range(M):
#                 for L in range(M):
#                     fly += N_list[i + k][j + L]
#             die_fly.append(fly)
#     print('#{0} {1}'.format(test_case, max(die_fly)))
