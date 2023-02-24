import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))
    sum_lst = []

    for left in range(N-M+1):
        right = left + M
        if right <= N:
            sum_lst.append(sum(v[left:right]))

    result = max(sum_lst)-min(sum_lst)

    print(f'#{test_case} {result}')
