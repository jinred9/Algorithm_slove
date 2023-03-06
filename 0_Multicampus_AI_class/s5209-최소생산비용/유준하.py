from itertools import permutations
testcase = int(input())
result = 999999
for tc in range(1, testcase+1):
    result = 999999
    number = int(input())
    making = [list(map(int, input().split())) for _ in range(number)]
    pe_making = list(permutations(making, number))
    for chk in pe_making:
        total = 0
        if result < total:
            break
        for i in range(0, number):
            total += chk[i][i]
        if result > total:
            result = total

    print(f"#{tc} {result}")
