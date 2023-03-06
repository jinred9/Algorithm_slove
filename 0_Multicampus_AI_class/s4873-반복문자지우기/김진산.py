import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    repeat_str = input()
    check = 0
    check_list = [0]
    for i in repeat_str:
        if i == check_list[check]:
            check_list.pop()
            check -= 1
        else:
            check_list.append(i)
            check += 1
    print(f"#{tc} {len(check_list)-1}")















