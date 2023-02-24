import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스
T = 10

for test_case in range(1, T + 1):
    # 건물 N 채
    N = int(input())
    # 조망권이 확보된 세대 수
    view = 0
    # 빌딩 높이 배열
    building = list(map(int, input().split()))
    # 0부터 시작시 0-2 = -2 98번 째 건물 높이 불러옴
    # N - 2를 끝점으로 index에서 벗어나지 않게함
    for i in range(2, N -2):
        # 좌우 2칸 이상 여백이 확보가 되어야  함으로 두칸씩 비교
        left_2 = building[i] - building[i + 2]
        left_1 = building[i] - building[i + 1]
        right_2 = building[i] - building[i - 1]
        right_1 = building[i] - building[i - 2]

        # 비교된 값들 중에서 가장 작은 값을 view에 저장
        if left_2 > 0 and left_1 > 0 and right_2 > 0 and right_1 > 0:
            view += min(left_2,left_1,right_2,right_1)
    print(f'#{test_case} {view}')

