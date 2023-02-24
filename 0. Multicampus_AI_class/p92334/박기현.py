def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report = list(set(report))
    report_dict = {}

    for target in report:
        idx, value = target.split()
        if idx in report_dict.keys():
            report_dict[idx].append(value)
        else:
            report_dict[idx] = []
            report_dict[idx].append(value)

    for id in id_list:
        cnt = 0
        for key in report_dict:
            if id in report_dict[key]:
                cnt += 1
        if cnt >= k:
            for idx, id2 in enumerate(id_list):
                if id2 in report_dict.keys():
                    if id in report_dict[id2]:
                        answer[idx] += 1

    return answer

# def solution(id_list, report, k):
#
#     answer = [0*m for m in range(len(id_list))]
#     report_lst = []
#     report_count = {}
#     report_dict = {}
#     report = list(set(report))
#
#     for target in report:
#         report_lst.append(target.split())
#         idx, value = target.split()
#         if idx in report_dict.keys():
#             report_dict[idx].append(value)
#         else:
#             report_dict[idx] = []
#             report_dict[idx].append(value)
#
#     print(report_dict)
#     print(report_lst)
#     for target in report_lst:
#         if target[1] not in report_count:
#             report_count[target[1]] = 1
#         else:
#             report_count[target[1]] += 1
#     freeze_lst = []
#     for key, value in report_count.items():
#         if value >= k:
#             freeze_lst.append(key)
#
#
#     for idx, id in enumerate(id_list):
#         if id in report_dict:
#             for freeze in freeze_lst:
#                 if freeze in report_dict[id]:
#                     answer[idx] += 1
#
#     return answer




    #
    # for target in report_target:
    #     cnt = 1
    #     for target2 in report_target:
    #         if target[0] != target2[0] and target[1] == target2[1]:
    #             cnt += 1
    #     if cnt >= k:
    #         for idx, val in enumerate(id_list):
    #             if target[0] == val:
    #                 answer[idx] += 1



print(solution(	["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
