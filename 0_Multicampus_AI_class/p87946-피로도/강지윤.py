def solution(k, dungeons):

    visited = [False for _ in range(len(dungeons))]
    Max = 0


    def dfs(left_hp, cleared_dungeons):

        nonlocal  Max
        if cleared_dungeons > Max:
            Max = cleared_dungeons

        for i in range(len(dungeons)):
            if not visited[i]:
                if left_hp >= dungeons[i][0]:
                    visited[i] = True
                    dfs(left_hp-dungeons[i][1], cleared_dungeons + 1)
                    visited[i] = False

    dfs(k, 0)
    return Max




print(solution(80,[[80,20],[50,40],[30,10]]))