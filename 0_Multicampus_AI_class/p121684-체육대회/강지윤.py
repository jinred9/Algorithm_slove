def solution(ability):
    answer = -1
    visited = [False for _ in range(len(ability))]
    space = len(ability[0])


    def dfs(Sum, index):
        nonlocal answer

        if index >= space:
            if Sum > answer:

                answer = Sum
            return

        for row in range(len(ability)):
            if not visited[row]:
                visited[row] = True
                dfs(Sum+ability[row][index], index+1)
                visited[row] = False

    dfs(0,0)
    return(answer)






print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))