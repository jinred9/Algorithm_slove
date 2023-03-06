testcase = int(input())

for tc in range(1, testcase + 1):
    N = int(input())
    N = N//10
    result = [0 for _ in range(0, 31)]
    for i in range(1, 31):
        if i == 1:
            result[i] = 1
        elif i == 2:
            result[i] = 3
        else:
            result[i] = result[i-1] + (2 * result[i-2])
    print(f"#{tc} {result[N]}")