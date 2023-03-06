import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    view_count = 0

    for i in range(2, N - 2):
        compare_h = max(height[i - 1], height[i - 2], height[i + 1], height[i + 2])
        if height[i] > compare_h:
            view_count += height[i] - compare_h
            # print(view_count)
    print(f'#{tc} {view_count}')


# N = 10
# height = [0,0, 3,5,2,4,9,0,6,4,0,6,0,0]
#
# view_count = 0
# for i in range(2, N+2):
#     compare_h = max(height[i-1], height[i-2], height[i+1], height[i+2])
#     if height[i] > compare_h:
#         view_count += height[i] - compare_h
#         print(view_count)
# print(view_count)