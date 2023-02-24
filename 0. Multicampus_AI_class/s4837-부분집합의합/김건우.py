import sys
sys.stdin = open('input.txt')


def dfs(idx):
    # 현재 idx 가 numbers의 길이와 같다 => 끝까지 갔다
    if idx == len(numbers):
        print(subset)
        print(visited)
        return

    subset.append(numbers[idx])
    visited[idx] = True

    dfs(idx+1)

    subset.pop()
    visited[idx] = False

    dfs(idx+1)


N, K = 3, 8
numbers = [1, 2, 3]

# 부분집합 / 포함 여부 둘 중에 하나만 있어도 됨
# 부분 집합
subset = []
# 포함 여부
visited = [False] * 3

count = 0
dfs(0)
print(count)


