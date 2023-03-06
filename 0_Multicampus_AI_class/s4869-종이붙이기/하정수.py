import sys

sys.stdin = open("input.txt", "r")
# 문제를 풀면 f(x) = f(x - 1) + 2 * f(x - 2)라는 점화식을 얻을 수 있다.
T = int(input())
for test_case in range(1, T + 1):
    hor = int(input()) / 10
    hor = int(hor)   # 가로 길이를 받아 10으로 나누어서 int 형태로 저장
    count = [0, 1, 3]   # 정답들의 초기값 설정 (계산을 쉽게하기 위해 맨앞에 0 추가)
    for n in range(3, hor + 1):
        count.append(count[n - 1] + 2 * count[n - 2])   # 점화식 계산
    print(f'#{test_case} {count[hor]}')
