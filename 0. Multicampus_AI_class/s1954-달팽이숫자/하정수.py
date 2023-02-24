import sys

sys.stdin = open("input.txt", "r")

T = int(input())

d_col = [1, 0, -1, 0]
d_row = [0, 1, 0, -1]

for test_case in range(1, T + 1):
    row = int(input())
    matrix = []
    heading = 0
    row_now = 0
    col_now = 0
    for _ in range(row):
        matrix.append([0] * row)

    for num in range(1, row ** 2 + 1):
        matrix[row_now][col_now] = num
        if row_now + d_row[heading] == row or col_now + d_col[heading] == row:
            heading += 1
            heading = heading % 4
        elif matrix[row_now + d_row[heading]][col_now + d_col[heading]] != 0:
            heading += 1
            heading = heading % 4

        row_now += d_row[heading]
        col_now += d_col[heading]

    print(f'#{test_case}')
    for i in range(row):
        print(*matrix[i])


# import sys
#
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     row = int(input())
#     matrix = []
#     for _ in range(row):
#         matrix.append([0] * row)
#
#     to_fill = row
#     row_now = 0
#     col_now = 0
#     heading = 1
#     done = 1
#     for _ in range(row * 2 - 1):
#         if heading % 4 == 1:
#             for num in range(to_fill):
#                 matrix[row_now][col_now] = done
#                 col_now += 1
#                 done += 1
#             heading += 1
#             row_now += 1
#             col_now -= 1
#
#         elif heading % 4 == 2:
#             to_fill -= 1
#             for num in range(to_fill):
#                 matrix[row_now][col_now] = done
#                 row_now += 1
#                 done += 1
#             heading += 1
#             col_now -= 1
#             row_now -= 1
#
#         elif heading % 4 == 3:
#             for num in range(to_fill):
#                 matrix[row_now][col_now] = done
#                 col_now -= 1
#                 done += 1
#             heading += 1
#             row_now -= 1
#             col_now += 1
#
#         elif heading % 4 == 0:
#             to_fill -= 1
#             for num in range(to_fill):
#                 matrix[row_now][col_now] = done
#                 row_now -= 1
#                 done += 1
#             heading += 1
#             col_now += 1
#             row_now += 1
#
#     print(f'#{test_case}')
#     for i in range(row):
#         print(*matrix[i])
