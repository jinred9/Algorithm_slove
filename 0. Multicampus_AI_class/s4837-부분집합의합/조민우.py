import sys
sys.stdin = open('input.txt')

def dfs(idx):
    global K, cnt, N
    # 현재 idx 가 numbers의 길이와 같다 => 끝까지 갔다
    if idx == len(numbers):
        # print(visited)
        if sum(subset) == K:
            if len(subset) == N:
                cnt += 1
        return

    subset.append(numbers[idx])
    # visited[idx] = True

    dfs(idx+1)

    subset.pop()
    # visited[idx] = False

    dfs(idx+1)

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    cnt = 0
    # numbers = [1, 2, 3]
    numbers = [_ for _ in range(1,13)]
    # 부분집합 / 포함 여부 둘 중에 하나만 있어도 됨
    # 부분 집합
    subset = []
    # 포함 여부
    # visited = [False] * 3
    count = 0

    dfs(0)

    print(f'#{test_case} {cnt}')






