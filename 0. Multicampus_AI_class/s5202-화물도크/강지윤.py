import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    numOfApplications = int(input())
    applications = []

    for a in range(numOfApplications):
        start, end = map(int, input().split())
        application = {}
        application['start'] = start
        application['end'] = end
        applications.append(application)

    applications.sort(key = lambda e : (e['start'],e['end']))
    count = 0
    end = None
    for a in applications:
        if end is None:
            end = a['end']
            count += 1

        if a['start'] >= end:
            end = a['end']
            count += 1
        else:
            if a['end'] < end:
                end = a['end']
            #시간이 겹치는 것중에 더 빨리 끝나는 걸로 end를 갱신시킨다.
    print(f'#{test_case} {count}')







