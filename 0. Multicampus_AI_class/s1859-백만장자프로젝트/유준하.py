
testcase = int(input())  # 테스트 케이스 입력
for tc in range(1, testcase+1):
    number = int(input())   # 테스트 케이스 별 자연수 N 입력
    prices = list(map(int, input().split()))  # 자연수 만큼의 가격 입력 받기
    maxprice = prices[-1]
    profit = 0
    for i in range(number-1, -1, -1):
        if prices[i] >= maxprice:
            maxprice = prices[i]
        else:
            profit += maxprice - prices[i]
    print(f"#{tc} {profit}")










