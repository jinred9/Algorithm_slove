# from collections import defaultdict
# def solution(id_list, report, k):
#    answer = []
#    user = defaultdict(set)
#    reported = defaultdict(int)
#    reportc= list(set(report))
#    for item in reportc:
#        nid, rid = item.split(' ')
#        user[nid].add(rid)
#        reported[rid] += 1
#
#    for i in id_list:
#        result=0
#        for j in user[i]:
#            if reported[j] >= k:
#                result += 1
#        answer.append(result)
#
#   return answer

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_count = {}
    history = {}
    for user in id_list:
        report_count[user] = 0
        history[user] = []

    for from_to in report:
        from_user, to_user = from_to.split()
        #중복 신청 제외
        if to_user not in history[from_user]:
            #신고내역에 추가
            history[from_user].append(to_user)
            #누적 신고 횟수 +1
            report_count[to_user] += 1

    #리스트에서 idx와 값을 동시에 꺼내기
    for idx, user in enumerate(id_list):
        #user의 신고내역(history)를 순회
        result=0
        for report_user in history[user]:
            #신고 횟수가 k 이상이면,
            if report_count[report_user] >= k:
                result += 1
        answer.append(result)
    return answer

