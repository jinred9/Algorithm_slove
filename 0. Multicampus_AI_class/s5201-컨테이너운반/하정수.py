import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    total = 0   # 총 운반량을 0으로 초기화
    N, M = map(int, input().split())
    cargos = [int(i) for i in input().split()]   # 화물 무게들과
    trucks = [int(i) for i in input().split()]   # 트럭의 최대 중량을 정수형으로 저장하고
    cargos.sort(reverse=True)   # 화물은 크기의 역순으로 정렬한다(무거운 것 부터 넣어보고 가장 무거운것 운송)
    for truck in trucks:   # 트럭 대수만큼
        for cargo in cargos:   # 화물의 중량이 무거운것 부터 비교하여
            if truck >= cargo:   # 트럭 최대 중량이 더 크면
                total += cargo   # 그 화물을 실어 나르고
                cargos.remove(cargo)   # 해당 화물을 화물 리스트에서 제거한다
                break   # 트럭은 한개밖에 적재할 수 없으므로 화물 선택 반복문을 종료한다

    print(f'#{test_case} {total}')
