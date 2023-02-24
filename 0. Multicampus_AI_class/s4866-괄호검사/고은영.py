import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = list(input())
    brace = 0 #중괄호
    braket = 0 #소괄호

    for i in string:
        if i == '{':
            brace +=1
        elif i == '}':
            brace -=1
        elif i == '(':
            braket +=1
        elif i == ')':
            braket -=1
    if brace ==0 and braket ==0:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {1}')
