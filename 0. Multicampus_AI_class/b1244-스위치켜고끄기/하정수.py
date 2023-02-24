import sys

sys.stdin = open("input.txt", "r")

T = int(input())
bulbs = list(map(int, input().split()))
student_num = int(input())
student = [list(map(int, input().split())) for _ in range(student_num)]

for change in range(student_num):
    if student[change][0] == 1:
        for number in range(1, T + 1):
            if number % student[change][1] == 0:
                if bulbs[number - 1] == 0:
                    bulbs[number - 1] = 1
                else:
                    bulbs[number - 1] = 0
    else:
        number = student[change][1]
        if number <= T - number:
            max_po = number - 1
        else:
            max_po = T - number

        if bulbs[number - 1] == 0:
            bulbs[number - 1] = 1
        else:
            bulbs[number - 1] = 0
        for distance in range(1, max_po + 1):
            if bulbs[number - 1 - distance] == bulbs[number - 1 + distance]:
                if bulbs[number - 1 - distance] == 1:
                    bulbs[number - 1 - distance], bulbs[number - 1 + distance] = 0, 0
                else:
                    bulbs[number - 1 - distance], bulbs[number - 1 + distance] = 1, 1
            else:
                break

for i in range(len(bulbs)):
    print(bulbs[i], end=' ')
    if (i + 1) % 20 == 0:
        print('')

