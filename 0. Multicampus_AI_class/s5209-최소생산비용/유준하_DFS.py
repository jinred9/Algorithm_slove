testcase = int(input())
def dfs(start, total):
    global result
    if result < total:
        return
    if start == number:
        if result > total:
            result = total
            return
    for works in range(number):
        if not made[works]:
            total += making[works][start]
            made[works] = True
            dfs(start+1, total)
            made[works] = False
            total -= making[works][start]


for tc in range(1, testcase+1):
    result = 999999
    number = int(input())
    made = [False] * number
    making = [list(map(int, input().split())) for _ in range(number)]
    dfs(0, 0)
    print(f"#{tc} {result}")

