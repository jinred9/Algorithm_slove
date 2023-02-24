# 입력 변수
# K : 충전후 최대 이동 가능 정류장 수
# N : 종점
# M : 충전기 설치된 정류장 수

# 목표
# 최소 몇 번의 충전후 종점에 도착할 수 있는지 출력
# 충전기가 잘못 설치되어 종점에 도착할 수 없는 경우 0 출력

# 출력
# #노선번호 최소_충전횟수

import sys

sys.stdin= open("input.txt", "r")
T = int(input())    # 노선 수

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())     # 입력변수
    gas = list(map(int, input().split()))  # 충전기 설치된 정류장 번호

    bus_stop = [0 for i in range(0, N+1)]   # 정류장 초기값 설정
    for i in range(0, M):
        bus_stop[gas[i]] = 1   # 충전기 정류장에만 1 설정

    loc = K    # 현재 위치
    count = 0   # 충전 횟수

    while 1:
        if bus_stop[loc] == 1:
            count += 1
            loc = loc+K
            fail = 0
            if loc >= N:
                break
        else:
            loc -= 1
            fail += 1
            if fail == K:
                count = 0
                break

    print(f"#{test_case} {count}")