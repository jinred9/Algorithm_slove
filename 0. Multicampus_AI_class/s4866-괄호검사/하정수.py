import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    sentence = input()   # 문장을 입력받는다
    checks = [0]   # 어떤 괄호가 열린 지 확인하고 저장하는 리스트를 초기화
    last = 0   # 마지막 괄호를 계산할 변수를 초기화

    for alph in sentence:
        if alph == '(':   # '(' 괄호가 열릴 때
            checks.append(1)   # 리스트에 1을 추가하고
            last += 1   # 마지막 번호를 1 늘려준다
        elif alph == '{':   # '{' 괄호일 때는
            checks.append(2)   # 2를 추가한다
            last += 1
        elif alph == ')':   # ')' 괄호가 닫히면
            if checks[last] == 1:   # 마지막에 '('로 열렸는지 확인하고
                checks.pop()   # 맞으면 pop을 하고
                last -= 1   # 마지막 번호를 1 줄여준다
            else:   # 맞지 않으면
                checks.append(0)   # 리스트에 0을 추가한다
        elif alph == '}':   # '}' 괄호가 닫히면
            if checks[last] == 2:   # 마지막에 '{'로 열렸는지 확인한다
                checks.pop()
                last -= 1
            else:
                checks.append(0)

    if checks == [0]:   # checks가 0만 있으면 1
        print(f'#{test_case} {1}')
    else:   # 다른 것들이 남아있으면 0
        print(f'#{test_case} {0}')

