import sys

sys.stdin = open('input.txt')


T = int(input())

now_dir = ([0,1],[1,0],[0,-1],[-1,0])
# 시계
now_loc = [0,0]
#현재 위치
flag = 0
#now dir의 현재 각도
for test_case in range(T):
    N = int(input())
    graph = [[0]*N for _ in range(N)]

    for num in range(1 ,N*N+1):
        graph[now_loc[0]][now_loc[1]] = num
        #그래프에선 x y 순서가 반대다
        new_r = now_loc[0] + now_dir[flag][0]
        new_c = now_loc[1] + now_dir[flag][1]

        if new_r >= N or new_c >= N or new_r < 0 or new_c < 0:
            flag += 1
            if flag > 3:
                flag = 0
            now_loc[0] = now_loc[0] + now_dir[flag][0]
            now_loc[1] = now_loc[1] + now_dir[flag][1]
        else :
            if graph[new_r][new_c] == 0:
                now_loc[0] = now_loc[0] + now_dir[flag][0]
                now_loc[1] = now_loc[1] + now_dir[flag][1]
            else:
                flag += 1
                if flag > 3:
                    flag = 0
                now_loc[0] = now_loc[0] + now_dir[flag][0]
                now_loc[1] = now_loc[1] + now_dir[flag][1]

    now_loc = [0,0]
    flag = 0
    print(f'#{test_case+1}')
    for r in range(N) :
        print(*graph[r])






















