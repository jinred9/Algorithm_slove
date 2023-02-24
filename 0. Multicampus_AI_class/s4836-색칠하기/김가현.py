# 입력
# N : 칠할 영역의 개수
# 왼쪽 위 인덱스, 오른쪽 아래 인덱스, 색상

# 출력
# 색이 겹치는 칸 수 (같은 색은 제외)

import sys

sys.stdin = open("input.txt", "r")

T = int(input())    # 테스트 케이스
for test_case in range(1, T+1):
    N = int(input())
    base = [[0 for i in range(10)] for j in range(10)]
    count = 0
    for k in range(1, N+1):
        rect = list(map(int, input().split()))
        for m in range(rect[0], rect[2]+1):
            for n in range(rect[1], rect[3]+1):
                if base[m][n] == 0:
                    if rect[4] == 1:
                        base[m][n] = 1
                    if rect[4] == 2:
                        base[m][n] = 2
                else:
                    if base[m][n] == rect[4]:
                        pass
                    else:
                        base[m][n] = 3

    for m in range(0, 10):
        for n in range(0, 10):
            if base[m][n] == 3:
                count += 1

    print(f"#{test_case} {count}")