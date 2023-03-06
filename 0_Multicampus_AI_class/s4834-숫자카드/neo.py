import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()
    card_count = [0] * 10

    for card in cards:
        card = int(card)
        card_count[card] += 1

    # 가장 큰걸 찾기 위해서 => 가장 작은 값을 설정
    max_count = 0
    # 현재 숫자카드들 중 아무거나 고른것
    max_value = 0
    for idx, count in enumerate(card_count):
        if count >= max_count:
            max_count = count
            max_value = idx

    print(f'#{tc} {max_value} {max_count}')
