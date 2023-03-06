import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sticks = input().replace('()', '*')
    print(sticks)

    # total 은 총 막대 개수
    # bar 는 열린 ( 의 숫자
    total = bar = 0

    for char in sticks:
        if char == '(':
            bar += 1
        elif char == ')':
            bar -= 1
            # 꼬다리 추가
            total += 1
        else:
            total += bar

    print(f'#{tc} {total}')
