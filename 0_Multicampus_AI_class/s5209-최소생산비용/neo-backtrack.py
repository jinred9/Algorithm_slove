import sys
sys.stdin = open('input.txt')


def backtrack(product_idx, total):
    global minimum
    if product_idx == N:
        if total < minimum:
            minimum = total
        return

    for factory_idx in range(N):
        if not visited[factory_idx]:
            visited[factory_idx] = True
            # new_total => 지금까지의 생산비용 + 이번 선택에 의한 생산비용
            new_total = total + matrix[product_idx][factory_idx]
            # 지금까지의 생산비용이 최소보다 작을 때만,
            if new_total < minimum:  # pruning => 가지치기
                backtrack(product_idx+1, new_total)
            visited[factory_idx] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    minimum = float('inf')
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]

    backtrack(0, 0)
    print(f'#{tc} {minimum}')
