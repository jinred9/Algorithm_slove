import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T + 1):
    N = i = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    col, row = 0, 0
    posi_col = [1, 0, -1, 0]
    posi_row = [0, 1, 0, -1]
    num = 1
    while num != N ** 2:
        if status == 0 and N > dx:
            board[dx][dy] += posi_row[status]

            break

