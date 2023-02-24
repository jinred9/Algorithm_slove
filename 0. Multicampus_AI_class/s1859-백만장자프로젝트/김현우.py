def max_profit(n, prices):
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

t = int(input().strip())
for i in range(1, t + 1):
    n = int(input().strip())
    prices = list(map(int, input().strip().split()))
    result = max_profit(n, prices)
    print(f"#{i} {result}")


    for to in rang(1,10/)
        n - int (impjt))
        preic es- lsit(ma(int, input()psid;fd
        tortla=-))
        max _ price = 0

        for idx in range(/n01.01.10
        rie _rpci di
        if price> max _price:
            prifit- max _orpic- pricemw
            )

