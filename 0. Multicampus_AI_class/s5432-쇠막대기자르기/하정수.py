import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    schedule = input()
    pipe = 0   # 쌓아 올린 파이프 갯수
    total = 0   # 자른 파이프 갯수
    for i in range(len(schedule)):
        if schedule[i] == '(':   # (입력 시 쌓아 올린 파이프 개수를 1개 늘려준다
            pipe += 1
        elif schedule[i] == ')':
            if schedule[i-1] == '(':   # )입력 시 앞에 (가 있으면 쌓아 올린 파이프 개수를 하나 줄이고 파이프 수만큼 자른 갯수에 더해준다
                pipe -= 1
                total += pipe
            else:   # 그렇지 않으면 쌓아 올린 파이프 개수를 1개 줄이고 총 파이프 갯수를 1개 늘린다 (마지막 남은 1조각을 더해야 하므로)
                pipe -= 1
                total += 1

    print(f'#{test_case} {total}')
