import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    chars = input()
    stack = []

    for char in chars:
        # 스택에 내용물이 있는데, 마지막 글자와 지금 보는 글자가 같다면,
        if stack and stack[-1] == char:
            stack.pop()
        # stack이 비어있다면,
        else:
            stack.append(char)

    answer = len(stack)
    print(f'#{tc} {answer}')
