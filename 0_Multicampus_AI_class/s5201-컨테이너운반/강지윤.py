import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    N,M = map(int, input().split())
    # N은 컨테이너 수, M 은 트럭의 수
    Containers_weight = list(map(int,input().split()))
    Containers_weight.sort()
    Truck_loading = list(map(int,input().split()))
    Truck_loading.sort(reverse=True)

    total_weight = 0

    for Truck in Truck_loading:

        if Containers_weight:
            container = Containers_weight.pop()
            #컨테이너 중 제일 큰거 뺌 이미 소팅해놨음
            if container > Truck:
                #만약 컨테이너의 무게가 트럭보다 클 경우 다음화물로 넘어감
                while Containers_weight:
                    container = Containers_weight.pop()
                    if container <= Truck:
                        total_weight += container
                        break
            else:
                total_weight += container

    print(f'#{test_case} {total_weight}')







