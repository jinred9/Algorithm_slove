import sys

sys.stdin = open('input.txt')
T = int(input())
# T = int(input())
# for test_case in range(1, T + 1):
#     txt = input()
#     # 괄호 입력받는 리스트
#     check_list =[]
#     # 입력받은 괄호의 위치
#     loc = 0
#     for check_txt in txt:
#         if check_txt == '(' or check_txt == '{':
#             check_list.append(check_txt)
#         elif check_txt == ')' or check_txt == '}':
#             if check_txt == ')' and check_list.pop() != '(':
#                 loc += 1
#             elif check_txt == '}' and check_list.pop() != '{':
#                 loc += 1
#     if loc == 0 and check_list:
#         print(f'#{test_case} {0}')
#     else:
#         print(f'#{test_case} {1}')


# 10 개중 8 개

for test_case in range(1, T + 1):
    txt = input()
    check_list =[0]
    for check_txt in txt:
        if check_txt == '(' or check_txt == '{':
            check_list.append(check_txt)
        elif (check_txt == '}' or ')'):
            if check_list.pop() != '{' or '(':
                break
        print(check_list)
    if check_list == []:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')
# for test_case in range(1, T + 1):
#     txt = input()
#     check_list =[]
#     for check_txt in txt:
#         if check_txt == '(' or check_txt == '{':
#             check_list.append(check_txt)
#         elif check_txt == '}' and check_list.pop() != '{':
#             break
#         elif check_txt == ')' and check_list.pop() != '(':
#             break
#     if check_list :
#         print(f'#{test_case} {0}')
#     else:
#         print(f'#{test_case} {1}')
