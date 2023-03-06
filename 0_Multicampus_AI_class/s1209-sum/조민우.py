import sys
sys.stdin = open('input.txt')


for test_case in range(1, 11):
    T = int(input())
    # ///////////////////////////////////////////////////////////////////////////////////
    array = []
    for i in range(100) :
        array.append(list(map(int, input().split())))

    # 가로줄의 합
    max_row = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += array[i][j]
        if sum > max_row :
            max_row = sum

    # 세로줄의 합
    max_col = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += array[j][i]
        if sum > max_col :
            max_col = sum

    # 대각선의 합
    max_diagonal = 0
    for i in range(100) :
        sum1 = 0 ; sum2 = 0
        sum1 += array[i][i]
        sum2 += array[i][-i]
    if max(sum1, sum2) > max_diagonal :
        max_diagonal = max(sum1, sum2)

    print(f"#{test_case} { max(max_row, max_col, max_diagonal)}")