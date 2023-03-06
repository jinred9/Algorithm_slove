
def solution(ability):
    total = 0
    # 노드 방문표시 위한 리스트 생성
    visited = [False for _ in range(len(ability))]
    def dfs(ab_sum, idx):
        nonlocal total
        # idx가 2차원 배열의 col값을 넘어가지 않게 범위 설정
        if idx >= len(ability[0]):
            # 새로운 값이 기존  값보다 크거나 같은 때 갱신
            if ab_sum >= total:
                total = ab_sum
            return
            # 깊이 탐색 종료후 전 노드로 리턴
        # ability의 길이를 가지고 visited에 방문여부 표시
        for i in range(len(ability)):
            if not visited[i]:
                visited[i] = True
                # ab_sum + ability[i][idx] 값을 통해서 종목별 ability 합산 도출
                # idx +1 해주며 다음 노드 탐색을 하게
                dfs(ab_sum + ability[i][idx], idx+1)
                visited[i] = False
    dfs(0,0)

    return total



print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))