import sys
sys.stdin = open('input.txt')

T = int(input())


def make_square(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    # Dynamic Programming => DP => 문제를 작은 문제로 쪼개서 접근하기
    return make_square(n-1) + make_square(n-2) * 2


def make_square2(n):
    # 최적화 => memoization => 기억 하기
    answers = [0, 1, 3]

    if n <= 2:
        return answers[n]

    for i in range(1, n+1):
        x = answers[i-1]
        y = 2 * answers[i-2]
        answers.append(x+y)

    return answers[n]


for tc in range(1, T+1):
    w = int(input()) // 10
    print(f'#{tc} {make_square(w)}')






