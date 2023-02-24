import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    numOfFactory = int(input())

    graph = [list(map(int, input().split())) for _ in range(numOfFactory)]

    visited = [False for _ in range(numOfFactory)]
    Minimum = float('inf')

    def dfs(Sum, product):
        global Minimum, visited
        if Minimum < Sum:
            return
        #이미 계산된 값보다 크면 더 진행할 필요없다.

        if product == numOfFactory:
            if Minimum > Sum:
                Minimum = Sum
            return
        #product가 row 인덱스를 의미한다. 트리의 높이를 조정한다.

        for i in range(numOfFactory):
            if not visited[i]:
                visited[i] = True
                dfs(Sum+graph[product][i], product+1)
                visited[i] = False


    dfs(0,0)
    print(f'#{test_case+1} {Minimum}')
