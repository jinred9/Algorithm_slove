import sys
sys.stdin = open('input.txt')

from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    minimum = float('inf')
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for case in permutations(range(N), N):
        total = 0

        for factory_idx, product_idx in enumerate(case):
            total += matrix[product_idx][factory_idx]
            if total >= minimum:
                break
        else:
            if total < minimum:
                minimum = total

    print(f'{tc} {minimum}')


