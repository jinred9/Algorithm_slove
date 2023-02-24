import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]
    max_val = 0
    for Ni in range(N - M + 1):
        for Nj in range(N - M + 1):
            sum_val = 0

            for Mi in range(M):
                for Mj in range(M):
                    sum_val += matrix[Ni + Mi][Nj + Mj]

                max_val = max(max_val, sum_val)

    print(f"#{tc} {max_val}")
