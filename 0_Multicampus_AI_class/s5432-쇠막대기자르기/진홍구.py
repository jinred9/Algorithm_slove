import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    n = input()
    n = list(n)
    poll_count = 0
    poll_cut = 0
    for i in range(len(n)):
        if n[i] == '(':
            poll_count += 1
        if i >= 1:
            if n[i] == ')' and n[i-1] != ')':
                poll_count -= 1
                poll_cut = poll_cut + poll_count
            if n[i] == ')' and n[i-1] == ')':
                poll_count -= 1
                poll_cut += 1
    print("#{} {}".format(test_case, poll_cut))