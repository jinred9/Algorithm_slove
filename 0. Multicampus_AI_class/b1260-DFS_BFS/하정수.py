import sys

sys.stdin = open('input.txt', 'r')

N, M, V = map(int, input().split())  # 정점, 간선, 시작 정점을 저장
edges = [[] for _ in range(N + 1)]  # 간선의 리스트 초기화

for _ in range(M):  # 간선의 리스트값 저장
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)

visited = [False for _ in range(N + 1)]  # 방문 기록 초기화
visited[V] = True  # 시작 정점을 이미 간 것으로 저장
to_visit = edges[V][:]  # 방문할 리스트
to_visit.sort()  # 오름차순 정렬
to_visit.reverse()  # 역순으로 재정렬(작은 수 부터 우측에서 pop하기 위해)

# DFS
order = [V]  # 검색기록을 저장할 order 리스트를 V로 초기화
while to_visit:
    current = to_visit.pop()  # pop을 시작하며
    if not visited[current]:  # 방문하지 않았다면
        visited[current] = True  # 방문 기록을 바꿔주고
        order.append(current)  # 검색 기록에 현재 정점을 추가
        c_to_visit = edges[current][:]  # 현재 정점의 간선을
        c_to_visit.sort()  # 정렬하여
        c_to_visit.reverse()  # 역순으로 재정렬 한 후
        to_visit += c_to_visit  # 방문할 리스트에 추가

print(*order)

# BFS
visited = [False for _ in range(N + 1)]  # DFS와 동일
visited[V] = True
to_visit = edges[V]
to_visit.sort()  # 역순으로 재정렬하지 않는다(좌측에서 pop하기 때문)

order = [V]
while to_visit:  # DFS와 동일
    current = to_visit.pop(0)
    if not visited[current]:
        visited[current] = True
        order.append(current)
        c_to_visit = edges[current][:]
        c_to_visit.sort()  # 역순으로 재정렬하지 않는다(좌측에서 pop하기 때문)
        to_visit += c_to_visit

print(*order)
