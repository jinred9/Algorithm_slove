import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # N : 컨테이너 수, M : 트럭 수
    N, M = list(map(int, input().split()))
    # w : 화물의 무게
    ws = list(map(int, input().split()))
    ws.sort()
    # t : 트럭의 중량
    ts = list(map(int, input().split()))
    ts.sort(reverse=True)
    total_weight = 0
    for t in ts:
        i = 0
        break_x = 0
        for j in range(len(ws)-1, -1, -1):
            if t >= ws[j] and break_x == 0:
                w_current = ws.pop(j)
                total_weight += w_current
                break_x += 1
    print(f'#{test_case} {total_weight}')


