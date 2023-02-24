import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    min_val = []
    max_val = []
    res = 0
    for _ in range(N):
        *list_all, color = list(map(int, input().split()))
        if color == 1:
            for i in range(list_all[0], list_all[2] + 1):
                for j in range(list_all[1], list_all[3] + 1):
                    min_val.append([i, j])

        else:
            for i in range(list_all[0], list_all[2] + 1):
                for j in range(list_all[1], list_all[3] + 1):
                    max_val.append([i, j])

    for min_res in min_val:
        for max_res in max_val:
            if min_res == max_res:
                res += 1

    print(f"#{tc} {res}")
