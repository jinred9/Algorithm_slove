import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    total = 0
    max_price = 0

    # 미래 부터 현재 까지 가격 확인
    for idx in range(N-1, -1, -1):
        # 지금 보고 있는 가격
        price = prices[idx]
        
        if price > max_price:
            # 팔아야 하는 가격
            max_price = price
        
        # 지금 가격이 팔아야 하는 가격보다 쌈
        else:
            # 고로 바로 이윤 계산 가능
            profit = max_price - price
            total += profit

    print(f'#{tc} {total}')
