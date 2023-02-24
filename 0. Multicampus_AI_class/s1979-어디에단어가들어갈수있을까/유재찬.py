import sys
sys.stdin = open("input.txt", "r")


def check_horizontal(ARR, i, j):
    if j - 1 >= 0 and ARR[i][j - 1] != 0:
        return False

    for k in range(j, j + M):
        if k >= N:
            return False
        if ARR[i][k] == 0:
            return False
    if j + M < N and ARR[i][j + M] == 1:
        return False
    return True


def check_vertical(ARR, i, j):
    if i - 1 >= 0 and ARR[i - 1][j] != 0:
        return False

    for k in range(i, i + M):
        if k >= N:
            return False
        if ARR[k][j] == 0:
            return False
    if i + M < N and ARR[i + M][j] == 1:
        return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR.append(list(map(int, input().split())))

    cnt = 0
    for i in range(N):
        for j in range(N):
            if check_horizontal(ARR, i, j):
                cnt += 1
            if check_vertical(ARR, i, j):
                cnt += 1

    print(f"#{test_case} {cnt}")
