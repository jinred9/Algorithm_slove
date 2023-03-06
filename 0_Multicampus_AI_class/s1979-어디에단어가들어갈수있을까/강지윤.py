import sys

sys.stdin = open('input.txt')

T = int(input())

for T in range(T):
    row,k = map(int,input().split())
    graph = []
    answer = 0
    for r in range(row) :
        graph.append(list(map(int,input().split())))


    for r in range(row):
        word_long = 0
        for c in range(row):
            if c == row - 1:
                if graph[r][c] == 1:
                    word_long+=1
                if word_long == k:
                    answer+=1
                break

            if graph[r][c] == 1:
                word_long+=1
            else:
                if word_long == k :
                    answer+=1
                word_long = 0

    for c in range(row):
        word_long = 0
        for r in range(row):
            if r == row - 1:
                if graph[r][c] == 1:
                    word_long+=1
                if word_long == k:
                    answer+=1
                break

            if graph[r][c] == 1:
                word_long += 1
            else:
                if word_long == k:
                    answer += 1
                word_long = 0


    print(f'#{T+1} {answer}')









