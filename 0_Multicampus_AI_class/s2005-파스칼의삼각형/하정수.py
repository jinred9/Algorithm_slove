import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())   # 삼각형의 높이를 저장한다.
    triangle = [[] for _ in range(num)]   # 높이만큼 리스트를 만들어준다.
    triangle[0] = [1]   # 꼭대기에 [1]을 넣어준다.

    for row in range(1, num):   # 두 번째 리스트 부터 마지막까지 반복한다.
        for n in range(row + 1):   # 높이만큼 가로로 반복 ex)위에서 2층 => 2번 반복
            if n == 0 or n == row:   # 양끝인 경우 1을 넣어준다.
                triangle[row].append(1)
            else:   # 이전 줄의 값으로부터 현재값을 저장한다.
                triangle[row].append(triangle[row - 1][n - 1] + triangle[row - 1][n])

    print(f'#{test_case}')
    for i in range(len(triangle)):
        print(*triangle[i])


