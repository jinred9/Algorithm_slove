import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))

    ARR = []
    for _ in range(N):
        ARR.append(list(map(int, input().split())))

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_val = 0
            for mi in range(i, i + M):
                for mj in range(j, j + M):
                    sum_val += ARR[mi][mj]
            max_sum = max(sum_val, max_sum)

    print(f"#{test_case} {max_sum}")
