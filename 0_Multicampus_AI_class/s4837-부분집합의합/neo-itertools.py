import sys
sys.stdin = open('input.txt')


#                        조합           순열
from itertools import combinations, permutations

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = [i for i in range(1, 13)]
    count = 0

    for case in combinations(numbers, N):
        if sum(case) == K:
            count += 1

    print(f'#{tc} {count}')


