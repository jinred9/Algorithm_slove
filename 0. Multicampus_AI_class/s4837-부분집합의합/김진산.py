import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = [i for i in range(1, N+1)]
    count = 0

    for i in combinations(numbers, N):
        if sum(i) == K:
            count += 1

    print(f"#{tc} {count}")


