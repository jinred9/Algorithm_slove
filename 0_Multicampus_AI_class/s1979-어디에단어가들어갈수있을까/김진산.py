import sys
sys.stdin = open("input.txt", "r")
# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
# [예제]
# N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때
# 길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로 4번)이 된다.


T = int(input())    # testcase를 받을 개수

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []  # 리스트를 입력할 빈 리스트
    result = 0  # 결과 값을 추가할 값
    for list_num in range(N):
        puzzle.append(list(map(int, input().split())))  # 퍼즐에 2차원 배열 추가

    for row in range(0, N):
        check = 0   # 배열을 체크할 변수 초기화 및 선언
        for column in range(0, N):   # 반복문을 두번 돌며 2차원 배열을 체크
            if puzzle[row][column] == 1:   # 해당 리스트 배열에 1이라는 숫자가 있을 시에 Check를 1 더함
                check += 1
            else:   # 아닐 경우
                if check == K:  # check의 값이 퍼즐의 단어 갯수인 K와 같은지 확인
                    result += 1     # 같을 경우 결과값을 1 추가
                check = 0       # 후 check 초기화

        if check == K:      # 반복문이 끝났을 때  check가 K와 같은지 확인
            result += 1

    for row in range(0, N):
        check = 0       # 배열을 체크할 변수 초기화 및 선언
        for column in range(0, N):   # 반복문을 두번 돌며 2차원 배열을 체크
            if puzzle[column][row] == 1:   # ij 의 순서를 바꿔 위아래로 훑으면서 리스트를 확인
                check += 1      # 해당 리스트 배열에 1이라는 숫자가 있을 시에 Check를 1 더함
            else:
                if check == K:  # check의 값이 퍼즐의 단어 갯수인 K와 같은지 확인
                    result += 1 # 같을 경우 결과값을 1 추가
                check = 0   # 후 check 초기화
        if check == K:  # 반복문이 끝났을 때  check가 K와 같은지 확인
            result += 1

    print(f"#{tc} {result}")



