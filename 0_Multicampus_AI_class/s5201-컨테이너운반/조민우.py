# N개의 컨테이너 M대의 트럭 A to B
# M대의 트럭 편도로 운반, 컨테이너마다 화물의 무게와 트럭의 적재용량 주어짐
# 화물의 총 중량이 최대 -> 화물의 전체 무게가 얼마인지 출력
# 컨테이너를 한 개도 옮길 수 없는 경우 0 출력

# 출력 값으로 화물의 전체 무게 or 0
from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # 컨테이너 수 , 트럭 대 수
    N, M = map(int, input().split())
    # 적재화물의 무게
    container = list(map(int, input().split()))
    # 컨테이너의 화물의 용량이 큰 순서대로 정렬
    container.sort(key=lambda x: -x)
    # 트럭 적재용량
    capacity = list(map(int, input().split()))
    capacity.sort(key=lambda x: x)
    # 현재 사용되는 트럭의 용량
    truck_cnt = 0
    # 트럭 적재 중량을 truck 반환받아 for문을 실행
    for truck in capacity:
        # 컨테이너 화물 중량을 weight 반환받아서 실행
        for weight in container:
            # 트럭의 적재가능 중량이 화물의 중량 이상일 경우 if문 실행
            if truck >= weight:
                # 트럭 적재된 화물의 중량
                truck_cnt += weight
                # 트럭이 적재가 가능 총 중량 - 적재된 화물의 중량
                truck -= weight
                # 중복되어서 적재되 않도록  적재된 화물 제거
                # 무거운 중량순으로 내림차순으로 정령 했기 떄문에 적재된 화물을 앞에서 부터 remove() 통해서 삭제
                container.remove(weight)
                # 하나의 트럭에 하나의 적재만 가능하기에 break으로 for문 탈출
                break

    print(f'#{test_case} {truck_cnt}')




