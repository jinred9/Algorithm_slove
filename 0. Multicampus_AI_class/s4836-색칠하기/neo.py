import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 색깔 좌표 갯수
    N = int(input())
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    count = 0

    # 색칠 시작
    for _ in range(N):
        # 시작 row 좌표, 시작 col 좌표, 끝 row 좌표, 끝 col 좌표, 색깔
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if matrix[r][c] != color:
                    matrix[r][c] += color
    globals()
    # 보라색 칸(3) 검사
    for r in range(10):
        for c in range(10):
            if matrix[r][c] == 3:
                count += 1

    print(f'#{tc} {count}')

