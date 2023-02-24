import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    rows = 10
    cols = 10
    arr = [[0 for j in range(cols)] for i in range(rows)]
    # n : 입력 수량
    n = int(input())
    for i in range(1, n + 1):
        globals()["sampling_case_{}".format(i)] = list(map(int, input().split()))
    for i in globals():
        start_col = 0
        if i.startswith("sampling") and globals()[i][-1] == 1:
            print(type(globals()[i]))