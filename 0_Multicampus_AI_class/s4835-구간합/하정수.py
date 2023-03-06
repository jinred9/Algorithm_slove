import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    length, check = list(map(int, input().split()))   # 전체 길이와 더하는 구간을 저장한다.
    numbers = list(map(int, input().split()))   # 전체 리스트를 저장한다.
    sum_max = sum_min = now = 0   # 구간합의 최대, 최솟값을 0으로 초기화한다.
    for n in range(check):
        sum_max += numbers[n]   # 첫구간의 구간합을 저장한다.
    sum_min = now = sum_max   # now라는 변수에 현재 구간합을 저장한다.

    for n in range(check, length):
        now = now + numbers[n] - numbers[n - check]   # 현재 구간합을 변경해준다.

        if now > sum_max:   # 현재 구간합이 최댓값보다 크면 대입한다.
            sum_max = now

        if now < sum_min:   # 현재 구간합이 최솟값보다 작으면 대입한다.
            sum_min = now

    sol = sum_max - sum_min

    print(f'#{test_case} {sol}')

