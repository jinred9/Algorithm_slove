import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    max_row, word_length = map(int, input().split())   # 단어 퍼즐의 크기와 단어의 길이를 저장한다
    puzzle = [list(map(int, input().split())) for _ in range(max_row)]   # 단어퍼즐을 리스트로 저장한다
    count = 0   # 가능한 횟수를 0으로 초기화 한다
    # 가로방향 계산
    for row in range(max_row):   # 가로열
        check = 0   # 연속된 1을 계산할 변수를 0으로 초기화 한다
        for column in range(max_row):   # 세로열
            if puzzle[row][column] == 1:
                check += puzzle[row][column]   # 현재 값이 1이면 연속 횟수에 1을 더해준다
                if check == word_length:
                    count += 1   # 연속 횟수가 단어 길이와 같다면 가능한 횟수를 1 더해준다
                elif check == word_length+1:
                    count -= 1   # 연속 횟수가 1개 더 늘어나면 가능한 횟수를 1 빼준다
            else:
                check = 0   # 현재 값이 1이 아니면 연속 횟수를 0으로 초기화 한다
    # 세로방향 계산
    # 가로열과 세로열의 반복 순서를 바꾸어 진행한다.
    for column in range(max_row):
        check = 0
        for row in range(max_row):
            if puzzle[row][column] == 1:
                check += puzzle[row][column]
                if check == word_length:
                    count += 1
                elif check == word_length+1:
                    count -= 1
            else:
                check = 0

    print(f'#{test_case} {count}')


