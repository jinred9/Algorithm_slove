import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    sell_price = 0
    total = 0
    last_day = prices[-1]
    for i in range(len(prices)-1, -1, -1):
        if prices[i] > last_day:
            last_day = prices[i]
        else:
            sell_price = last_day - prices[i]
            total += sell_price

    print(f'#{tc} {total}')