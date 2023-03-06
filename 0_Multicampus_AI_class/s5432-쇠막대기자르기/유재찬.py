


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    ROW = input()

    s = []
    cnt = 0
    prev = ""
    for r in ROW:
        if r == "(":
            s.append(r)
        else:
            s.pop()
            if prev == "(":
                cnt += len(s)
            else:
                cnt += 1
        prev = r

    print(f"#{test_case} {cnt}")