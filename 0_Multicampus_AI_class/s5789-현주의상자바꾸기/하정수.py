import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    box, kind = map(int, input().split())   # 박스의 총 갯수와 숫자의 갯수를 저장
    box_list = [list(map(int, input().split())) for _ in range(kind)]   # 각 숫자가 몇번부터 몇번까지 변하는지 저장
    box_name = [0] * box   # 박스 갯수만큼 0으로 초기화
    for num in range(kind):   # 변하는 숫자 갯수만큼 반복
        for change in range(box_list[num][0] - 1, box_list[num][1]):   # 변하는 숫자의 범위만큼 반복
            box_name[change] = num + 1   # 변하는 숫자 입력

    print(f'#{test_case}', end=' ')
    for box in range(box):
        print(box_name[box], end=' ')
    print('')
