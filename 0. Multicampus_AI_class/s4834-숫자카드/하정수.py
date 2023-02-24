import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    length = int(input())   # 입력 개수를 저장한다.
    numbers = [int(n[0:1]) for n in input()]   # 입력값들을 저장한다.
    minimum = 0   # 가장 많이 나온 횟수를 0으로 초기화한다.
    max_num = 0   # 가장 많이 나온 숫자를 0으로 초기화한다.

    for i in range(10):   # 0부터 10까지 반복
        if numbers.count(i) >= minimum:   # i의 개수를 세어 최댓값보다 크면 그 숫자와 갯수를 저장한다.
            minimum = numbers.count(i)
            max_num = i

    print(f'#{test_case} {max_num} {minimum}')
