import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수
T = int(input())

for tc in range(1, T + 1):
    # 퍼즐의 크기 N, 단어의 길이  K 단어수
    N, K = map(int, input().split())

    # 2차원 배열의 퍼즐
    puzzle = []
    for line in range(N):
        puzzle.append(list(map(int, input().split())))

    # 단어의 길이를 만족
    found_word = 0

    # 가로줄 탐색
    for row in range(0, N):
        # 단어의 길이
        word_length = 0
        for column in range(0, N):
            if puzzle[row][column] == 1:
                word_length += 1
            else:
                if word_length == K:
                    found_word += 1
                word_length = 0
        if word_length == K:
            found_word += 1

    # 세로줄 탐색
    for row in range(0, N):
        # 단어의 길이
        word_length = 0
        for column in range(0, N):
            if puzzle[column][row] == 1:
                word_length += 1
            else:
                if word_length == K:
                    found_word += 1
                word_length = 0
        if word_length == K:
            found_word += 1

    print(f"#{tc} {found_word}")