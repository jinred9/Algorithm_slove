import sys
sys.stdin = open('input.txt')

T = 10
N = 100

for tc in range(1, T + 1):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = []
    for row in range(N):
        row_num = 0
        col_num = 0
        line_num = 0
        reversed_num = 0
        for col in range(N):
            row_num += arr[row][col]
            col_num += arr[col][row]
            line_num += arr[col][col]
            reversed_num += arr[-col][-col]
        temp.append(row_num)
        temp.append(col_num)
        temp.append(line_num)
        temp.append(reversed_num)
    print(f"#{tc} {max(temp)}")


