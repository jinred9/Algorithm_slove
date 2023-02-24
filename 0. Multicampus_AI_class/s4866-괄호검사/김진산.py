import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    char = str(input().split())
    first_in_list = []
    pop_list = []
    text = 0
    cnt = 0
    temp = 0
    temp1 = 0
    res = 0
    for char in char:
        if char == '(' or char == ')' or char == '{' or char == '}':
            first_in_list.append(char)
    while first_in_list:
         text = first_in_list.pop()
         pop_list.append(text)

         if pop_list[-1] == ')' or pop_list[-1] == '}':
            temp = pop_list.pop()
            temp1 = first_in_list.pop()
            if temp == ')' and temp1 == '(':
                cnt += 1
            elif temp == '}' and temp1 == '{':
                cnt += 1
            else:
                first_in_list.append(temp1)
                pop_list.append(temp)
         if len(first_in_list) == 0:
             temp = pop_list.pop()
             temp1 = pop_list.pop()
             if temp == '(' and temp1 == ')':
                 cnt += 1
             elif temp == '{' and temp1 == '}':
                 cnt += 1
             else:
                 pop_list.append(temp)
                 pop_list.append(temp1)

         if len(first_in_list) == 0 and len(pop_list) == 0:
             res += 1

    print(f"#{tc} {res}")




