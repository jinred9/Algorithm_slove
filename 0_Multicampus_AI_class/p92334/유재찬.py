def solution(id_list, report, k):
    answer = []

    report_dict = {user_id: set() for user_id in id_list}
    report_count = {user_id: 0 for user_id in id_list}

    for line in report:
        user_id, reported_id = line.split(" ")
        report_dict[user_id].add(reported_id)

    for user_id, reported_id_set in report_dict.items():
        for reported_id in reported_id_set:
            report_count[reported_id] += 1

    for user_id, reported_id_set in report_dict.items():
        count = 0
        for reported_id in reported_id_set:
            if report_count[reported_id] >= k:
                count += 1
        answer.append(count)

    return answer
