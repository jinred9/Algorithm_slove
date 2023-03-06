testcase = int(input())

for i in range(1, testcase+1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    maps = []
    killfly = []
    for x in range(N):
        maps.append(list(map(int, input().split())))
    for j in range(0, N-M+1):       # N-M+1
        for k in range(0, N-M+1):   # N 이 5이고 M이 2일 경우 가로 기준 4번 세로 기준 4번 연산
            sum= 0
            for kj in range(M):
                for kk in range(M):
                    sum += maps[kj+j][kk+k]
            killfly.append(sum)       # 리스트에 처치한 파리수를 모두 저장
    print(f"#{i} {max(killfly)}")     # 리스트 중 최대값 출력
