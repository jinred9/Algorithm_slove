import sys

sys.stdin = open('input.txt')

T = int(input()) #테스트케이스 개수

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    max = 0


    for i in range(N-(M-1)): #초기 셀 선택 (가로)
        for j in range(N-(M-1)):  #초기 셀 선택(세로)

            sum = 0
            for a in range(M): #값 순회 (가로)
                for b in range(M): #세로
                    sum += array[i+a][j+b] #i,j를 더함으로써 시작점 좌표를 지정해줌 (M이 2일때 a,b는 0,1)
                if sum > max:
                    max = sum

    print(f'#{tc} {max}')