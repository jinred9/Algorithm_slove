import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedules = [list(map(int, input().split())) for _ in range(N)]
    schedules.sort(key=lambda x: x[1])
    # 마지막 작업이 끝나는 시간
    last = 0
    # 총 할 수 있는 일의 개수
    count = 0

    for start, end in schedules:
        # 새로 시작하는 일이 마지막 일보다 같거나 늦게 끝난다면,
        if start >= last:
            last = end
            count += 1

    print(f'#{tc} {count}')
