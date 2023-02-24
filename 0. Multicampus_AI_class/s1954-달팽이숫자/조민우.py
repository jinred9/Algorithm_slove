import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    num = 1
    row = col = 0
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]
    idx = 0
    matrix[row][col] = 1
    while num != N ** 2:

        new_row = row + d_row[idx]
        new_col = col + d_col[idx]

        if 0 <= new_row < N and 0 <= new_col < N and matrix[new_row][new_col] == 0:
            num += 1
            row, col = new_row, new_col

            matrix[row][col] = num

        else:
            # 꺾는다.
            idx = (idx + 1) % 4

    print(f'#{test_case}')
    for line in matrix:
        print(*line)

