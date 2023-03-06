def get_cnt(n, m):
    cnt = 0
    while n % m == 0:
        n /= m
        cnt += 1
    return cnt


T = int(input())


for test_case in range(1, T + 1):
    N = int(input())
    a = get_cnt(N, 2)
    b = get_cnt(N, 3)
    c = get_cnt(N, 5)
    d = get_cnt(N, 7)
    e = get_cnt(N, 11)
    print(f"#{test_case} {a} {b} {c} {d} {e}")
