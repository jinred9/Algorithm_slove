# ==================================================================
# 최적화 필요
# ==================================================================

import sys
sys.stdin = open('input.txt')

# 스위치 총 수량
sw_num = int(input())
# 스위치 상태
sw_status = list(map(int, input().split()))
# 학생 수
student_num = int(input())
for test_case in range(1, student_num + 1):
    # x : 남(1), 여(2) 구분
    # y : 해당학생 위치
    x, y = map(int, input().split())
    if x == 1: # 남학생
        i = 1
        y_mul = y
        while y_mul <= sw_num:
            if sw_status[y_mul - 1] == 1:
                sw_status[y_mul - 1] = 0
            else:
                sw_status[y_mul - 1] = 1
            i += 1
            y_mul = y * i  # 남학생은 자신의 수의 배수 스위치 바꾸기
    # print(sw_status)

    elif x == 2: # 여학생
        min_y = y - 2   # 주어진 sw보다 -1값 index
        max_y = y       # 주어진 sw보다 +1값 index
        if sw_status[y - 1] == 1:
            sw_status[y - 1] = 0
        else:
            sw_status[y - 1] = 1
        while min_y >= 0 and max_y <= (sw_num - 1):
            if sw_status[min_y] == sw_status[max_y]:
                if sw_status[min_y] == 1:
                    sw_status[min_y] = 0
                    sw_status[max_y] = 0
                else:
                    sw_status[min_y] = 1
                    sw_status[max_y] = 1
            else:
                break
            min_y -= 1
            max_y += 1
        # print(sw_status)

sw_text = ""
add_blank = " "
add_line = " \n"
i = 1
for _ in sw_status:
    if i % 20 == 0:
        sw_text = sw_text + str(_) + add_line
    else:
        sw_text = sw_text + str(_) + add_blank
    i += 1

sw_text = sw_text.rstrip()
print(sw_text)
