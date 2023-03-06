import sys

sys.stdin = open('input.txt')

T = int(input())

# for test_case in range(1, T + 1):
#     text = list(input())
#     stack = [0]
#     check = 0
#     count = 0
#     for text_letter in text:
#         if text_letter == '}':
#             if '{' != stack.pop():
#                 stack.append(text_letter)
#         elif text_letter == ')':
#             if '(' != stack.pop():
#                 stack.append(text_letter)
#         elif text_letter == '{':
#             count += 1
#             stack.append(text_letter)
#         elif text_letter == '(':
#             count += 1
#             stack.append(text_letter)
#     if len(stack) == 1 and count > 0:
#         check = 1
#     elif
#         check = 0
#     print(f'#{test_case} {check}')
#
