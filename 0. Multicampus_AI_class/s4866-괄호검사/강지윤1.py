import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    String = input()
    stack = []

    for char in String :
        if char == '(' or char == '{':
            stack.append(char)

        if char == '}' or char == ')':
            if not stack:
                stack.append('fail')
                break

            if char == '}':
                if stack.pop() == '(':
                    stack.append('fail')
                    break
            elif char == ')':
                if stack.pop() == '{':
                    stack.append('fail')
                    break

    if stack:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')

