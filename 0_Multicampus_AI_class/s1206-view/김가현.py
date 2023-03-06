# N : 건물의 개수 (4 <= N <= 1000)
# 양 옆으로 2칸 이상의 공백 존재시 조망권 확보

import sys
sys.stdin = open("input.txt", "r")

T = 10  #테스트 케이스
for test_case in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))    # 건물의 높이
    count = 0   # 조망권 확보된 세대의 수
    for i in range(2, N-1):
        max_height = 0
        fail = 0
        for j in range(i-2, i):     # 왼쪽 조망권 확인
            if fail >= 1:
                pass
            else:
                if height[j] >= height[i]:
                    fail += 1
                else:
                    if height[j] >= max_height:
                        max_height = height[j]
        if fail == 0:
            for k in range(i+1, i+3):   # 오른쪽 조망권 확인
                if fail >= 1:
                    pass
                else:
                    if height[k] >= height[i]:
                        fail += 1
                    else:
                        if height[k] >= max_height:
                            max_height = height[k]

        if fail >= 1:
            max_height = height[i]

        count += (height[i]-max_height)
    print(f"#{test_case} {count}")
