import sys

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
    # 좌표에서 R, B 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                R_location = [i, j]
            if arr[i][j] == 'B':
                B_location = [i, j]
    current = R_location
    count = 0
    to_visits = [current]
    while to_visits:
        current = to_visits.pop()
        if not visted[current[0]][current[1]]:
            visted[current[0]][current[1]] = True
        # 오른쪽으로 이동
        move_hori = 0
        move_ver = 0
        if R_location[1] < B_location[1]:
            move_ver = 1
        elif R_location[1] > B_location[1]:
            move_ver = -1
        elif R_location[0] < B_location[0]:
            move_hori = 1
        elif R_location[0] > B_location[0]:
            move_hori = -1

        count += 1
        while arr[B_location[0] + move_hori][B_location[1] + move_ver] == '.':
            arr[B_location[0] + move_hori][B_location[1] + move_ver] = 'B'
            arr[B_location[0]][B_location[1]] = '.'
        while arr[R_location[0] + move_hori][R_location[1] + move_ver] == '.':
            arr[B_location[0] + move_hori][B_location[1] + move_ver] = 'R'
            arr[B_location[0]][B_location[1]] = '.'
        for i in [-1, 1]:
            if arr[R_location[0]][R_location[1]+i] == '.':
                to_visits.append([R_location[0], R_location[1]+i])
            if arr[R_location[0]+i][R_location[1]] == '.':
                to_visits.append([R_location[0]+i, R_location[1]])
        if arr[R_location[0] + move_hori][R_location[1] + move_ver] == 'O' or arr[B_location[0] + move_hori][B_location[1] + move_ver] == 'O':
            to_visits = False

    if count > 10 or count == -1:
        count = -1

    print(count)