import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(T):

    graph = [ [0] * 10 for i in range(10)]

    numOfColor = int(input())
    interleaved_point = 0
    for square in range(numOfColor):
        p1_x, p1_y, p2_x, p2_y, color  = map(int, input().split())

        for row in range(p1_x, p2_x+1):
            for col in range(p1_y, p2_y+1):
                if graph[row][col] == 0:
                    graph[row][col] = color
                elif color != graph[row][col]:
                    graph[row][col] = 3
                    interleaved_point+=1

    print(f'#{test_case+1} {interleaved_point}')










