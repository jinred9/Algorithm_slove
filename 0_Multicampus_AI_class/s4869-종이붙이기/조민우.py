import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def make_square(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    # Dynamic Programing => DP
    return make_square(n-1) + 2 * make_square(n-2)
def make_square2(n):
    if n <= 1:
        return answers[n]

    for i in range(2, n+1):
        x = answers[i - 2]
        y = 2 * answers[i - 1]
        answers.append(x + y)

    return answers[n]
for test_case in range(1, T + 1):
    N = int(input()) // 10

    print(f'#{test_case} {make_square(N)}')

# def fibo(n):
#     answer = [0,1]
#     if n <= 1:
#         return n
#     for i in range(2, n+1):
#         x = answer[i-2]
#         y = answer[i-1]
#         answer.append(x+y)
#     return answer(n)

# def nCr(n, ans, r):
#     if n == len(nums):
#         if len(ans) == r:
#             temp = [i for i in ans]
#             answer_list.append(temp)
#         return
#     ans.append(nums[n])
#     nCr(n + 1, ans, r)
#     ans.pop()
#     nCr(n + 1, ans, r)
#
#
# for test_case in range(1, T + 1):
#     N = int(input())
#
#     width = N
#     height = 20
#
#     # 20으로 넣을 씨 개수
#     num = N//20
#     # 10으로 넣을 시 개수
#     var = N//10
#
#     # 직사각형이 경우의 수
#     small_count = 0
#     # 정사각형이 경우의 수
#     big_count = 0
#     # 직사각형이 채워진 개수
#     small = 0
#     # 정사각형이 채워진 개수
#     big = 0
#     i = 1
#
#     # c문제 3c3 = 1
#     # 3!/3
#     while i <= num:
#         a = 20 * i
#         k = width // a
#         print('k',k)
#         q = width - a
#         print('q',q)
#         nums = [_ for _ in range(k+1)]
#         print(nums)
#         nCr(0, [], q//10)
#         print(len(answer_list))
#         i+=1
#



