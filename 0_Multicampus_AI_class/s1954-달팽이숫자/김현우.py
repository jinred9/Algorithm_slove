def solution(n):
    dx = [0, 1, 0, -1]  # x 방향 이동
    dy = [1, 0, -1, 0]  # y 방향 이동
    x, y, c = 0, -1, 1  # 시작 위치 및 시작 숫자
    a = [[0]*n for _ in range(n)]  # 배열 초기화

    for k in range(n*2-1):  # 전체 이동 횟수
        for i in range((n - (k % n)) // 2):  # 현재 단계에서 이동하는 횟수
            x, y = x + dx[k % 4], y + dy[k % 4]
            a[x][y] = c
            c += 1

    return a