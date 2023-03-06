T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_kills = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kills = sum(grid[x][y] for x in range(i, i+M) for y in range(j, j+M))
            if kills > max_kills:
                max_kills = kills