import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    sentence = input()
    stack = []

    for s in sentence:
        if not stack :
            stack.append(s)
            continue

        if s == stack[len(stack)-1]:
            stack.pop()
        else :
            stack.append(s)

    print(f'#{test_case} {len(stack)}')





