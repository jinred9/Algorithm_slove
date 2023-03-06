
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    ROWS = []
    for _ in range(Q):
        ROWS.append(list(map(int, input().split())))

    boxes = [0 for _ in range(N)]
    for idx, (L, R) in enumerate(ROWS):
        for i in range(L - 1, R):
            boxes[i] = idx + 1
    print(f"#{test_case} {' '.join(map(str, boxes))}")
