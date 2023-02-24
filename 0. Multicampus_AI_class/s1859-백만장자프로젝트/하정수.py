import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 계산을 위해 가격 리스트를 뒤집는다
    numbers.reverse()
    profit = 0
    # 마지막날 가격을 기준으로 전날이 더 저렴하면 차액만큼 이익을 추가하고 전날이 더 비싸면 새로운 기준으로 설정한다
    max_price = numbers[0]
    for now in range(1, N):
        if max_price >= int(numbers[now]):
            profit = profit + max_price - int(numbers[now])
        else:
            max_price = int(numbers[now])
    print(f'#{test_case + 1} {profit}')
