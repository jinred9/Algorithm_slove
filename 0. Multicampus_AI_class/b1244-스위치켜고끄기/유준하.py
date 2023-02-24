
tc = int(input())
switch= list(map(int, input().split()))
switch.insert(0,0)
def change(num1):
    if switch[num1] == 0:
        switch[num1] = 1
    else:
        switch[num1] = 0

student = input()
student = int(student)
for i in range(0, student):
    gender, num = input().split()
    num = int(num)
    gender = int(gender)
    if gender == 1:
        for x in range(1, tc+1):
            if x % num == 0:
                change(x)
    elif gender == 2:
        check = []
        for y in range(1, (tc//num)+1):
            if num - y < 1 or num + y > tc:
                break
            else:
                if switch[num-y] == switch[num+y]:
                    check.append(y)
        maxcheck = max(check)
        for k in range(num-maxcheck, num+maxcheck+1, 1):
            change(k)

for i in range(tc):
    print(switch[i+1], end=' ')
    if (i + 2) % 20 == 0:
        print('')



def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0

