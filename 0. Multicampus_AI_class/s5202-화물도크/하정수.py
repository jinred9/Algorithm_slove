import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    schedules = []
    n = int(input())
    for _ in range(n):
        schedules.append(input().split())
    schedules.sort(key=lambda schedule: (int(schedule[1]), int(schedule[0])))
    end = int(schedules[0][1])
    count = 1
    for car_num in range(1, n):
        if int(schedules[car_num][0]) >= end:
            end = int(schedules[car_num][1])
            count += 1
    print(f'#{test_case} {count}')
