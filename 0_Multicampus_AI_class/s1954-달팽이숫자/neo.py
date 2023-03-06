import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    # 채울 숫자
    num = 1
    # 델타 탐색
    d_rows = [0, 1, 0, -1]
    d_cols = [1, 0, -1, 0]
    idx = 0
    # 초기화
    row = col = 0
    board[row][col] = 1

    # 언제까지 반복..?
    while num != N ** 2:
        # 이동하고자 하는 곳의 좌표 값
        new_row = row + d_rows[idx]
        new_col = col + d_cols[idx]
        # 좌표 갱신 가능(범위 맞고, 기존에 칠한적 없고)
        if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == 0:
            num += 1
            # 현재 위치를 새로운 위치로 갱신
            row, col = new_row, new_col
            # 갱신한 위치에 숫자 적기
            board[row][col] = num
        # 좌표 갱신이 불가능하면,
        else:
            # 꺾는다.
            idx = (idx+1) % 4

    print(f'#{tc}')
    for line in board:
        print(*line)
