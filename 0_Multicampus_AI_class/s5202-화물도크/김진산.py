import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = []
    count = 0
    work_time = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: (x[1], x[0]))
    for i in range(len(arr)):
        s, e = arr[i]
        if work_time <= s:
            count += 1
            work_time = e
    print(f"#{tc} {count}")


