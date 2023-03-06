import sys

sys.stdin = open("input.txt", "r")
for test_case in range(1, 11):
    T = int(input())   # 테스트케이스 설정에 주의, n번째인 것을 하나씩 빼주어야한다.
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]   # 사다리를 100X100 리스트로 받아준다.
    now = []   # 역으로 찾아갈 위치를 정의한다.
    for col in range(100):
        if ladder_matrix[99][col] == 2:   # 정답 위치를 찾아 저장한다. # 맨밑에서 좌우로 움직일 수 없으므로 99대신 98 사용
            now = [98, col]

    while now[0] > 0:   # 맨 윗줄에 도착할 때 까지 반복한다.
        if now[1] == 0:   # 좌측 끝인 경우
            if ladder_matrix[now[0]][now[1] + 1] == 1:   # 오른쪽이 1인 경우
                ladder_matrix[now[0]][now[1]] = 0   # 현재 값을 0으로 바꿔주고
                now = [now[0], now[1] + 1]   # 오른쪽으로 이동
            else:   #아닌 경우
                now = [now[0] - 1, now[1]]   # 위로 한줄 이동

        elif now[1] == 99:   # 우측 끝인 경우 좌측 경우와 좌우이동과 반대
            if ladder_matrix[now[0]][now[1] - 1] == 1:
                ladder_matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] - 1]
            else:
                now = [now[0] - 1, now[1]]

        else:   # 양 끝이 아닌경우 좌, 우를 다 확인한다.
            if ladder_matrix[now[0]][now[1] + 1] == 1:
                ladder_matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] + 1]

            elif ladder_matrix[now[0]][now[1] - 1] == 1:
                ladder_matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] - 1]

            else:
                now = [now[0] - 1, now[1]]

    print(f'#{test_case} {now[1]}')
