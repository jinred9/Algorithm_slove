import sys
from collections import deque

sys.stdin = open('input.txt')

N, M, S = map(int, input().split())

graph = [[] for i in range(1001)]
#그래프

visited = [False for i in range(1001)]

for _ in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

to_visit = [S]
dfs = []
while to_visit :
    current = to_visit.pop()
    graph[current].sort(reverse=True)
    if not visited[current]:
        dfs.append(current)
        visited[current] = True
        to_visit += graph[current]

print(*dfs)

visited = [False for i in range(1001)]
to_visit.append(S)
bfs = []
while to_visit :
    current = to_visit.pop(0)
    graph[current].sort()
    if not visited[current]:
        bfs.append(current)
        visited[current] = True
        to_visit += graph[current]

print(*bfs)

















