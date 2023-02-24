import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # k : 한번 이동가능한 수
    # n : 총 정류장 수
    # m : 충전기 수량
    k, n, m = map(int, input().split())
    # charge_location : 충전기 위치
    charge_location = list(map(int, input().split()))
    # bus 현재 위치 초기값
    bus = [0]
    # bus 이동시 위치 초기값
    next_bus = 0
    while next_bus < n:
        next_bus = bus[-1] + k
        # charge_count는 충전기위치를 1번만 하기 위한 변수
        charge_count = 0
        # charge_count 저장값
        for _ in range(bus[-1] + k, bus[-1], -1):
            if next_bus in charge_location and charge_count == 0:
                bus.append(next_bus)
                charge_count = 1
                #충전
            elif next_bus not in charge_location:
                next_bus -= 1
                #next_bus  값 감소시킴
            if _ == bus[-1] + 1 :
                next_bus = n
                bus = [0]
        next_bus = next_bus + k

    print("#{} {}".format(test_case, len(bus) - 1))

