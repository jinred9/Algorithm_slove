import sys

sys.stdin = open('input.txt')

switch_num = int(input())
switch_state = list(map(int, input().split()))
switch_state.insert(0, float('inf'))
#넘버링 맞춰 주려고 리스트 맨앞에 inf 추가


for _ in range(int(input())):
    gender, number = map(int,input().split())
    if gender == 1:
        for i in range(1,len(switch_state)):
            if i%number == 0:
                if switch_state[i] == 1:
                    switch_state[i] = 0
                else:
                    switch_state[i] = 1

    else:
        if switch_state[number] == 1:
            switch_state[number] = 0
        else:
            switch_state[number] = 1

        for i in range(1,switch_num):
            if number-i <=0 or number+i >switch_num:
                break

            if switch_state[number+i] == switch_state[number-i]:
                if switch_state[number+i] == 1:
                    switch_state[number+i] = switch_state[number-i] = 0
                else:
                    switch_state[number + i] = switch_state[number - i] = 1
            else:
                break


for i in range(1,len(switch_state)):
    print(switch_state[i], end=' ')
    if (i) % 20 == 0:
        print()











