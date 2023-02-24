tc = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(1, tc+1):
    N = int(input())
    maps = [[0]*N for _ in range(N)]
    x, y = 0, 0
    direction = 0
    for step in range(1, N*N+1):
        maps[x][y] = step
        x += dx[direction]
        y += dy[direction]
        if x < 0 or x >= N or y < 0 or y >= N or maps[x][y] != 0:    #벽을 만났을 때 즉 x, y 의 위치가 맵을 벗어나면 방향 전환
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]
    print(f"#{i}")
    for all in maps:
        print(*all)
