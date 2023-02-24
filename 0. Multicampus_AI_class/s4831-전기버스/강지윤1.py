import sys

sys.stdin = open('input.txt')

T = int(input())


for test_case in range(T):
    K, N, M = map(int,input().split())
    # K 한번 충전시 이동할 수 있는 거리
    # N : 마지막 정류장 번호
    # m : 충전기 수량

    charge_place = list(map(int,input().split()))
    current_place = 0
    charge_count = 0

    while(True):
        if current_place + K >= N:
            print(f'#{test_case} {charge_count}')
            break

        for step in range(K, 0, -1):

            if step == 1 and current_place + step not in charge_place:
                charge_count = 0
                current_place = float('inf')
                break


            if current_place + step in charge_place:
                current_place += step
                charge_count += 1
                break



