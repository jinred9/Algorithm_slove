# 입력
# N : 정수의 개수 (10 <= N <= 100)
# M : 구간의 개수 (2 <= M < N)

# 이웃한 M개의 합을 계산
# 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램 작성

import sys
import math
sys.stdin = open("input.txt", "r")

T = int(input())    # 테스트 케이스
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # 입력 변수
    num = list(map(int, input().split()))  # 입력배열 리스트로 변환

    loc = 0     # 위치
    sum_max = -math.inf     # 합계 최대값
    sum_min = math.inf     # 함계 최소값

    while 1:
        sum_M = 0  # 합계
        for i in range(loc, loc+M):
            sum_M += num[i]

        if sum_M >= sum_max:     # 합계 최대최소 비교
            sum_max = sum_M
        if sum_M <= sum_min:
            sum_min = sum_M

        loc += 1
        if loc+M > N:
            break

    ans = sum_max - sum_min     # 출력값

    print(f"#{test_case} {ans}")