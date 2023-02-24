import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T+1):

    answer = 1
    stack = []
    code = input()
    for char in code:
        if char in '(){}':
            # 열리는 괄호면 무조건 스택에 추가
            if char in'({':
                stack.append(char)
            # 닫히는 괄호면,
        elif char in '(){}':
                # 스택이 비어있는데, 닫히는게 나왔다면 에러
                if not stack:
                    answer = 0
                    break

                last = stack.pop()
                # 열림 닫힘이 일치하지 않음 => 에러
                if (char == ')' and last != '(') or (char == '}' and last != '{'):
                    answer = 0
                    break

            # 끝까지 다 봤는데 찌꺼기가 남아있음 => 애러
            if stack:
                answer = 0
        else:
            continue

    print(f'#{test_case} {answer}')