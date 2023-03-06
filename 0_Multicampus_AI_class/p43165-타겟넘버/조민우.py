from itertools import combinations
def solution(numbers, target):
    for idx in range(1,len(numbers)+1):
        for num in combinations(numbers,idx):


    return


# def solution(numbers, target):
#     answer = 0
#     count = 0
#     df_cnt = 0
#
#     def cal_number(idx,sum_result_def,numbers_def,target_def):
#         nonlocal count
#         if idx == len(numbers_def):
#             if sum_result_def == target_def:
#                 count += 1
#             # 끝가지 탐색한 함수 종료
#             return
#
#         cal_number(idx+1,sum_result_def+numbers_def[idx],numbers_def,target_def)
#         cal_number(idx+1,sum_result_def-numbers_def[idx],numbers_def,target_def)
#
#     cal_number(0,0,numbers,target)
#     return count

# print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))