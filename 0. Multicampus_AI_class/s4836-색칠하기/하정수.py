import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    coloring = int(input())   # 칠하는 색 횟수를 저장한다.
    matrix = [[0 for _ in range(10)] for _ in range(10)]   # 10X10 배열에 0을 대입하여 초기화한다.
    info_of_colors = [list(map(int, input().split())) for _ in range(coloring)]   # 칠하는 색 정보를 저장한다.
    purple = 0   # 보라색이 된 칸의 갯수를 0으로 초기화한다.

    for n in range(coloring):   # 좌상단, 우하단의 값을 저장한다.
        row_now = info_of_colors[n][0]
        col_now = info_of_colors[n][1]
        row_to = info_of_colors[n][2] + 1
        col_to = info_of_colors[n][3] + 1

        if info_of_colors[n][4] == 1:   # 빨간색을 칠하는 경우
            for r in range(row_now, row_to):
                for c in range(col_now, col_to):   # 좌상단, 우하단의 범위를 순회한다.
                    if matrix[r][c] == 2:   # 현재 파란색이 칠해져있으면 보라색을 칠해준다.
                        purple += 1
                    else:
                        matrix[r][c] = 1   # 아니면 빨간색을 칠해준다.

        elif info_of_colors[n][4] == 2:   # 빨간색과 반대로 진행한다.
            for r in range(row_now, row_to):
                for c in range(col_now, col_to):
                    if matrix[r][c] == 1:
                        purple += 1
                    else:
                        matrix[r][c] = 2

    print(f'#{test_case} {purple}')



