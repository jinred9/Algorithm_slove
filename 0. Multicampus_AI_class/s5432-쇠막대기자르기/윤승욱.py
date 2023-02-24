T = int(input())
for tc in range(1, T+1):
    iron_bar = input()

    cnt = 0 # 막대 수
    ans = 0 # 정답

    for i in range(len(iron_bar)):
        # 막대 추가
        if iron_bar[i] == '(':
            cnt += 1
        else:
        # 닫힌 괄호라면 막대가 감소한다.
            cnt -= 1

            # 레이저
            if iron_bar[i-1] == '(':
                ans += cnt
            else:
            # 막대 끝이라는 뜻이다.
                ans += 1

    print("#{} {}".format(tc, ans))
