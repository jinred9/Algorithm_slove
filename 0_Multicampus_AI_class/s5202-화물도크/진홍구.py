import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    request_times = [list(map(int, input().split())) for _ in range(N)]
    request_times.sort()
    request_times.sort(key=lambda x: x[1])
    count = 0
    last_time = 0
    for i in range(len(request_times)):
        start, end = request_times[i]
        if i == 0:
            last_time = end
            count += 1
        elif last_time <= start:
            last_time = end
            count += 1
    print(f'#{test_case} {count}')



    # count = 0
    # count_last = 0
    # for i in range(len(request_times)):
    #     start_pre, end_pre = request_times[i-1]
    #     start_now, end_now = request_times[i]
    #     if i == 0:
    #         start_now, end_now = request_times[i]
    #         scheduled_time.append(start_now)
    #         scheduled_time.append(end_now)
    #     elif i > 0:
    #         start_pre, end_pre = request_times[i - 1]
    #         start_now, end_now = request_times[i]
    #     if scheduled_time[-1] >= end_now and count_last != 0:
    #         i -= 1
    #     elif scheduled_time[-1]
