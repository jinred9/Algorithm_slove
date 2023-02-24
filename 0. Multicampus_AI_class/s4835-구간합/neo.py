import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 그냥 최초에 확인할 수 있는 구간을 최대 이자 최소로 설정
    min_value = max_value = sum(numbers[0:M])

    for left in range(N-M+1):
        right = left + M
        segment_sum = sum(numbers[left:right])
        if segment_sum < min_value:
            min_value = segment_sum
        elif segment_sum > max_value:
            max_value = segment_sum

    result = max_value - min_value
    print(f'#{test_case} {result}')
