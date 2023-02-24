import sys
sys.stdin = open('input.txt')


def dfs(idx):
    global count

    # 현재 idx 가 numbers의 길이와 같다 => 부분 집합 완성
    if idx == len(numbers):
        # 조건을 만족했다면, count 추가
        if len(subset) == N and sum(subset) == K:
            count += 1
        return

    subset.append(numbers[idx])
    dfs(idx+1)
    # visited[idx] = True

    subset.pop()
    dfs(idx+1)
    # visited[idx] = False


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = [i for i in range(1, 13)]

    # 부분집합 / 포함 여부 둘 중에 하나만 있어도 됨
    # 부분 집합
    subset = []
    # 포함 여부
    # visited = [False] * 12

    count = 0
    dfs(0)
    print(f'#{tc} {count}')


