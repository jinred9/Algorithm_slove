import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    a = list(input())
    dic = {}
    max_val = 0
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    res_key = '1'
    sort_key = sorted(dic)
    for k in sort_key:
        if dic[k] >= max_val:
            max_val = dic[k]
            res_key = k

    print(f"#{test_case} {res_key} {max_val}")

















