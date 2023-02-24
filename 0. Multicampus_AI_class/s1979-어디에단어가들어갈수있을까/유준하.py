testcase = int(input())

for i in range(1, testcase+1):
    count = 0
    N, K = input().split()
    N = int(N)
    K = int (K)
    maps = []
    for x in range(N):
        maps.append(list(map(int, input().split())))
    # 가로
    for j in range(0, N):
        check = 0
        for k in range(0, N):
            if maps[j][k] == 1:
                check += 1
            else:
                if check == K:
                    count += 1
                    check = 0
                else:
                    check = 0
        if check == K:
            count += 1

    # 새로
    for j in range(0, N):
        check = 0
        for k in range(0, N):
            if maps[k][j] == 1:
                check += 1
            else:
                if check == K:
                    count += 1
                    check = 0
                else:
                    check = 0
        if check == K:
            count += 1
    print(f"#{i} {count}")
