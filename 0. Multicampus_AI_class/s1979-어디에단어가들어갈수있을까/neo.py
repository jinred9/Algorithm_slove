import sys
sys.stdin = open('input.txt')

T = int(input())

N, K = map(int, input().split())

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix.append(row)

matrix = [list(map(int, input().split())) for _ in range(N)]

# 행 탐색
for row in range(N):
    for col in range(N):
        print(matrix[row][col])

# 열 탐색
for col in range(N):
    for row in range(N):
        print(matrix[row][col])


# 대각 탐색
for i in range(N):
    print(matrix[i][i])

for j in range(N):
    print(matrix[i][N-1-i])
