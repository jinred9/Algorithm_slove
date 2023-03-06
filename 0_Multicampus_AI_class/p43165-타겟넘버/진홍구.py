# 재귀함수로 풀이 ==============================================================
def solution1(numbers, target):
    answer = 0
    def dfs_def(sum, index):
        nonlocal answer
        if index == len(numbers):
            if sum == target:
                answer += 1
            return
        dfs_def(sum + numbers[index], index + 1)
        dfs_def(sum - numbers[index], index + 1)
    dfs_def(0, 0)
    return answer

# 배열로 풀이 ==============================================================
from itertools import product
dataset = [1, -1]
def solution2(numbers, target):
    answer = 0
    arr_basic = list(product(dataset, repeat = len(numbers)))
    for arr_each in arr_basic:
        sum = 0
        for i in range(len(arr_each)):
            sum += arr_each[i] * numbers[i]
        if sum == target:
            answer += 1
    return answer

print(solution1([1, 1, 1, 1, 1], 3))
print(solution1([4, 1, 2, 1], 4))
print(solution2([1, 1, 1, 1, 1], 3))
print(solution2([4, 1, 2, 1], 4))

# 하정수 정답..=================================================
# def solution(numbers, target):
#     count = 0   # target을 만들 수 있는 횟수를 0으로 초기화한다
#     numbers_copy = numbers[:]
#
# # 덧셈을 해주는 DFS함수
#     def dfs(sum_now, index, k):
#         nonlocal count
#         if k == 1:
#             numbers_copy[index-1] = 1
#         elif k == -1:
#             numbers_copy[index-1] = -1
#         if index == len(numbers):   # index가 더할 숫자들의 갯수와 같은 경우
#             if sum_now == target:   # 현재 합이 target과 같다면
#                 count += 1   # count 수를 1개 늘려주고
#             return   # 반환한다
# # +, - 두개의 분기가 있는 DFS이므로 재귀의 횟수는 2번 진행한다
#         dfs(sum_now + numbers[index], index + 1, 1)
#         dfs(sum_now - numbers[index], index + 1, -1)
#
#     dfs(0, 0, 0)
#     return count
#
# numbers = [1, 1, 1, 1, 1]
# target = 3
# print(solution(numbers, target))
# numbers = [4, 1, 2, 1]
# target = 4
# print(solution(numbers, target))