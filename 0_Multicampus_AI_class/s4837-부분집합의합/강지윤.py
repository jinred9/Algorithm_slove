import sys

sys.stdin = open("input.txt", "r")

T = int(input())    # 테스트 케이스


def dfs(idx):
    global count, subset

    if idx == len(numbers):
        return

    if len(subset) == N:
        if sum(subset) == K:
            count += 1
        return

    subset.append(numbers[idx])
    dfs(idx + 1)
    subset.pop()
    dfs(idx + 1)


for test_case in range(T):

    N, K = map(int,input().split())
    #숫자의 수, 숫자의 합
    count = 0
    numbers = [i for i in range(1,13)]
    # 표본공간
    subset = []
    dfs(0)
    print(f'#{test_case} {count}')






