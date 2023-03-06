import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))

    min_val = float('inf')
    max_val = 0
    for i in range(N - M + 1):
        v = sum(ARR[i:i + M])
        min_val = min(v, min_val)
        max_val = max(v, max_val)

    print(f"#{test_case} {max_val - min_val}")
