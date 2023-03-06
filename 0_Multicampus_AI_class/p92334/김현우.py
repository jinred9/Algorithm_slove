def solution(id_list, report, k):
    count = {}
    for user in id_list:
        count[user] = 0
    for r in report:
        reported = r.split()[1]
        count[reported] += 1
    result = [0 for _ in range(len(id_list))]
    for i, user in enumerate(id_list):
        for r in report:
            if r.startswith(user + " "):
                reported = r.split()[1]
                if count[reported] >= k:
                    result[i] += 1
                    break
    return result