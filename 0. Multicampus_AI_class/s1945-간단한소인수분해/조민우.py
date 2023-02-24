import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())

    cal = [2, 3, 5, 7 ,11]
    count = [0,0,0,0,0]

    x = 0
    for i in cal:
        y = 0
        while 1:
            if N % i == 0:
                N = N // i
                y += 1
                count[x] = y

            else:
                break
        x += 1
    print(f"#{test_case} {' '.join(map(str,count))}")


