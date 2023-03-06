def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_count = [0] * len(id_list)
    dict = {}

    for i in id_list:

    # 신고를 먼저 분류
    for i in report:
        post_user, receive_user = i.split(" ")
        if receive_user not in dict[post_user]:
            print(receive_user)
    # 중복 여부 확인

    # 신고 횟수 확인

    # 신고 보낸사람 횟수 확인
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
               2))

print(solution(["con", "ryan"],
               ["ryan con", "ryan con", "ryan con", "ryan con"],
               3))