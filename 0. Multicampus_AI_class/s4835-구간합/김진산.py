import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_val = 0
    min_val = 0
    arr1 = []
    res = 0
    for col in range(N - M + 1):
        increase = 0
        sum_val = 0
        sum_ = 0
        for i in range(M):
            sum_ += arr[col + i]

        arr1.append(sum_)
        max_val = max(arr1)
        min_val = min(arr1)
    res = max_val - min_val
    print(f"#{tc} {res}")












