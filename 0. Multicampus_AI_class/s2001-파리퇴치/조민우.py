import sys

sys.stdin = open('input.txt')

T = int(input()) #테스트케이스 개수

for tc in range(1, T + 1):
    N, K = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    SumList = []
    for i in range(N-K-1):
        for j in range(N-K-1):

            sum = 0
            for F_C in range(K):
                for F_R in range(K):
                    sum += matrix[i+F_C][j+F_R]
                SumList.append(sum)

    print(f'#{tc} {max(SumList)}')