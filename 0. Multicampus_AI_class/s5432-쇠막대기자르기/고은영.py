import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    stick = input().replace('()', '*')

    result = 0
    bar = 0

    for i in stick:
        if i == '(' :
            bar += 1
        elif i == ')' :
            bar -= 1
            result +=1 #(마지막 꼬다리 막대)
        else :
            result += bar
    print(result)


