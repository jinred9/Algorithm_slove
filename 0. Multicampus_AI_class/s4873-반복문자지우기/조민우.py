import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    sent = input()
    check = []

    for txt in sent:
        if check and txt == check[-1]:
            check.pop()
        else:
            check.append(txt)

    print(f'#{test_case} {len(check)}')
