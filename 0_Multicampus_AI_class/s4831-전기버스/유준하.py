testcase = int(input())
for i in range(1, testcase+1):
    N, K, M = map(int, input().split())
    pos, answer = 0, 0
    batt_stat = list(map(int, input().split()))
    while pos != N:
        move = pos + K
        if move >= N:
            pos = N
            break
        for x in range(len(batt_stat)-1, -1, -1):
            if move >= batt_stat[x]:
                pos = batt_stat[x]
                answer += 1
                batt_stat = batt_stat[x+1:]
                break
            if x == 0:
                answer = 0
                pos = N
    print(answer)
