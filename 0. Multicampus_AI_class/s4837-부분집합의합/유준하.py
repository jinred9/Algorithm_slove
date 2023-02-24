from itertools import combinations

testcase = int(input())
for tc in range(1, testcase+1):
    count = 0
    N, K = map(int, input().split())
    numbers = [i for i in range(1, 13)]
    combi_list = list(combinations(numbers, N))
    for items in combi_list:
        if sum(items) == K:
            count += 1

    print(f"#{tc} {count}")