import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    battery, total_len, charge = map(int, input().split())   # 배터리 길이, 전체 길이, 충전소 갯수를 저장
    charge_list = list(map(int, input().split()))   # 충전소의 위치를 저장
    charge_list.reverse()   # 충전소 위치를 역순으로 바꾼다.
    charge_list.append(0)   # 마지막에 처음 충전한 시작점을 추가해준다.
    charged = 0   # 충전횟수를 0으로 초기화해준다.
    back = total_len   # 뒤에서부터 역으로 계산할 것이므로 마지막자리를 저장
    before = 0   # 충전소를 지나쳐서 온 거리를 저장
    for i in range(charge + 1):   # 출발지점을 추가했기때문에 1을 더해준다.
        distance = back - charge_list[i]   # 이동한 거리를 저장해준다.

        if distance > battery:   # 이동한 거리가 배터리보다 크면 0을 반환시켜준다.
            charged = 0
            break

        if before + distance <= battery:   # 이전이동거리와 지금 이동거리의 합이 이동가능거리보다 적으면 이전에 충전한 것을 빼준다.
            charged -= 1

        else:   # 그렇지 않으면 충전했으므로 이전 이동거리를 0으로 초기화 한다.
            before = 0

        back = charge_list[i]   # 현 위치를 이전 충전소로 이동시킨다.
        charged += 1   # 충전 횟수를 1 증가시켜준다.
        before += distance   # 이전이동거리를 현재 이동한 거리로 설정해준다.

    print(f'#{test_case} {charged}')
