import sys
sys.stdin = open('input.txt')


def dfs(idx):
    global count
    # 현재 idx 가 numbers의 길이와 같다 => 끝까지 갔다
    if idx == len(numbers):
        if len(subset) == N and sum(subset) == K:
            count += 1
        return

    subset.append(numbers[idx])
    dfs(idx+1)
    subset.pop()
    dfs(idx+1)


numbers = [i for i in range(1, 13)]

# 부분집합 / 포함 여부 둘 중에 하나만 있어도 됨
# 부분 집합

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    subset = []
    count = 0
    dfs(0)
    print(f'#{test_case} {count}')


