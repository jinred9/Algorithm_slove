testcase = int(input())

cal = [2, 3, 5, 7, 11]
for i in range(1, testcase+1):
    answer = []
    number = int(input())
    for items in cal:
        count = 0
        while 1:
            if number % items == 0:
                number = number / items
                count += 1
            else:
                break
        answer.append(count)
    print(f"#{i} {' '.join(map(str,answer))}")
