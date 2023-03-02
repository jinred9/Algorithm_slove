import sys
import copy

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N : 세로, M : 가로
    N, M = map(int, input().split())
    # visted 초기화
    visted = [[False for _ in range(M)] for _ in range(N)]
    # 입력된 자표 초기화
    arr = []
    # 좌표 matrix로 만들기
    for _ in range(N):
        arr.append(list(input()))
    print(arr)
    moving = []
    # 좌표에서 R, B 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                R_location = [i, j]
            if arr[i][j] == 'B':
                B_location = [i, j]
    count = 0
    move_hori = 0
    move_ver = 0
    to_direction = 1
    to_visits_direction = [R_location, B_location]
    while to_visits_direction:

        to_visits_B = to_visits_direction.pop()
        to_visits_R = to_visits_direction.pop(0)
        to_destination = [0]
        for move_hori, move_ver in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            current = to_visits_R[:]
            R_location = to_visits_R[:]
            B_location = to_visits_B[:]
            to_arr = copy.deepcopy(arr)
            for _ in range(2):
                while to_arr[B_location[0] + move_hori][B_location[1] + move_ver] == '.':
                    to_arr[B_location[0] + move_hori][B_location[1] + move_ver] = 'B'
                    to_arr[B_location[0]][B_location[1]] = '.'
                    B_location[0] += move_hori
                    B_location[1] += move_ver
                while to_arr[R_location[0] + move_hori][R_location[1] + move_ver] == '.':
                    to_arr[R_location[0] + move_hori][R_location[1] + move_ver] = 'R'
                    to_arr[R_location[0]][R_location[1]] = '.'
                    R_location[0] += move_hori
                    R_location[1] += move_ver
            if current != R_location:
                to_destination[R_location] = B_location

        to_visits_direction.append(to_destination)



















    # def find_red(move_ver, move_hori, R_location, count, visted):
    #     global return_count
    #     current = R_location[:]
    #
    #     # 오른쪽으로 이동
    #     if R_location[1] < B_location[1] and move_ver != -1:
    #         move_ver = -1
    #     elif move_ver == -1:
    #         move_ver = 1
    #     elif R_location[0] < B_location[0] and move_hori != -1:
    #         move_hori = -1
    #     elif move_hori == -1:
    #         move_hori = 1
    #     for _ in range(2):
    #         while arr[B_location[0]+move_hori][B_location[1]+move_ver] == '.':
    #             arr[B_location[0]+move_hori][B_location[1]+move_ver] = 'B'
    #             arr[B_location[0]][B_location[1]] = '.'
    #             B_location[0] += move_hori
    #             B_location[1] += move_ver
    #         while arr[R_location[0]+move_hori][R_location[1]+move_ver] == '.':
    #             arr[R_location[0]+move_hori][R_location[1]+move_ver] = 'R'
    #             arr[R_location[0]][R_location[1]] = '.'
    #             R_location[0] += move_hori
    #             R_location[1] += move_ver
    #     if not visted[current[0]][current[1]] and current != R_location and not visted[R_location[0]][R_location[1]]:
    #         visted[current[0]][current[1]] = True
    #     if visted[R_location[0]][R_location[1]] == True and current != R_location and visted[R_location[0]][R_location[1]]:
    #         print('aaa')
    #         return
    #     elif arr[R_location[0] + move_hori][R_location[1] + move_ver] == 'O' or arr[B_location[0] + move_hori][B_location[1] + move_ver] == 'O':
    #         return
    #     elif count > 10:
    #         return
    #     else:
    #         count += 1
    #     for i in [-1, 1]:
    #         if arr[R_location[0]][R_location[1]+i] == '.':
    #             find_red(move_ver, move_hori, [R_location[0], R_location[1]], count, visted)
    #         if arr[R_location[0]+i][R_location[1]] == '.':
    #             find_red(move_ver, move_hori, [R_location[0], R_location[1]], count, visted)
    #
    #
    # find_red(move_ver, move_hori, R_location, count, visted)
    #
    # if return_count > 10 or return_count == -1:
    #     return_count = -1

    # print(count)