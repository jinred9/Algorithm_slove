import sys
sys.stdin = open('input.txt')
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    building_heights = list(map(int, input().split()))
    # 조망권이 확보된 세대
    view_house = 0
    # 현재 건물 위치
    for i in range(2, N-2):
        if building_heights[i] > max(building_heights[i-2], building_heights[i-1], building_heights[i+1], building_heights[i+2]):
            view_house += building_heights[i] - max(building_heights[i-2], building_heights[i-1], building_heights[i+1], building_heights[i+2])
    print(f'#{test_case} {view_house}')
