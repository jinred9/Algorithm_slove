












# 실패한 프로그램
# def solution(gems):
#     answer = []
#     arr1 = list(set(gems)) # 중복제거
#     i = 0
#     j = 0
#     last_num = 0
#     for i in range(len(gems)):
#         try:
#             arr1.remove(gems[i])
#         except:
#             pass
#         if not arr1 and j == 0:
#             last_num = i + 1
#             i = len(gems)
#             j += 1
#         i += 1
#     i = 0
#     j = 0
#     set_list = ()
#     for i in range(last_num - 1, -1, -1):
#         set_list = gems[i : last_num]
#         if set(set_list) == set(gems) and j == 0:
#             first_num = i + 1
#             j += 1
# 
#     answer.append(first_num)
#     answer.append(last_num)
#     return answer





print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB", "YYY", "NNNN", "YYY", "BBB"]))
