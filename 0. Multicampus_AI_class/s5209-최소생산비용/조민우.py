# 첫줄 제품수 N, 생산비용 v가 주어짐

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    V_len = len(V)
    V_col_len = len(V[0])
    # 노드 방문표시 위한 리스트 생성
    visited = [False for _ in range(len(V))]
    total = float('inf')
    def dfs(v_sum, idx):
        global total
        # idx가 2차원 배열의 col값을 넘어가지 않게 범위 설정
        if idx == V_col_len:
            # 새로운 값이 기존  값보다 크거나 같은 때 갱신
            if v_sum < total:
                total = v_sum
            return
        # total 값이 어느 위치에 있든지 v_sum 값 이하 일때 탐색의 의미가 없으므로 중간에 return
        if total <= v_sum:
            return
        # V의 길이를 가지고 visited에 방문여부 표시
        for i in range(V_len):
            if not visited[i]:
                visited[i] = True
                # idx +1 해주며 다음 노드 탐색을 하게
                dfs(v_sum + V[i][idx], idx + 1)
                visited[i] = False

    dfs(0, 0)
    print(f'#{test_case} {total}')

    # https://80000coding.oopy.io/85650ea5-e541-4b12-9b86-a958a99b7533 백트래킹 설명