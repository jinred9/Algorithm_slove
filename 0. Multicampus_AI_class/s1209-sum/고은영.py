import sys
sys.stdin = open('input.txt')




for tc in range(10): #tc = 10개
    T = int(input())
    arr = []

    for i in range(100):
        array =list(map(int,input().split()))
        arr.append(array)


    #가로
    max_r = 0
    for i in range(100): #100행 반복
        summation = 0
        for j in range(100): #100열 반복하여 합산
            summation += arr[i][j]

        if summation > max_r:
            max_r = summation

    #세로
    max_c = 0
    for i in range(100):  # 100행 반복
        summation = 0
        for j in range(100):  # 100열 반복하여 합산
            summation += arr[j][i]
        if summation > max_c:
            max_c = summation



    # 대각선 \,/
    max_d = 0
    for i in range(100):
        sum1 = 0
        sum2 = 0
        sum1 += arr[i][i]
        sum2 += arr[i][99 - i]
    if max(sum1, sum2) > max_d:
        max_d = max(sum1, sum2)

    print("#{} {}".format(T, max(max_r, max_c, max_d)))