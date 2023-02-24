import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    build_height = list(map(int, input().split()))
    right = 0
    left = 0
    res = 0
    for i in range(2, len(build_height)-2):
        if build_height[i-1] >= build_height[i-2]:
            left = build_height[i-1]
        else:
            left = build_height[i-2]

        if build_height[i + 1] >= build_height[i + 2]:
            right = build_height[i + 1]
        else:
            right = build_height[i + 2]

        if build_height[i] > left and build_height[i] > right:
            res += build_height[i] - max(left,right)
    print(f"#{tc} {res}")

