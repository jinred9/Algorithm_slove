def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    # 신고 횟수
    report_count = {}

    # 신고 내역
    history = {}
    # 초기 데이터 세팅
    for user in id_list:
        report_count[user] = 0
        history[user] = []

    # 신고 내역 추가/신고 횟수 누적
    for from_to in report:
        from_user, to_user = from_to.split()
        # 중복 신고 여부
        if to_user not in history[from_user]:
            # 신고 내역에 추가
            history[from_user].append(to_user)
            # 누적 신고 횟수 +1
            report_count[to_user] += 1

    # 리스트에서 idx와 값을 동시에 꺼내기
    for idx, user in enumerate(id_list):
        # user의 신고내역(history)를 순회
        for report_user in history[user]:
            # report_user의 신고 횟수가 k 이상이면,
            if report_count[report_user] >= k:
                # 신고한 사람(user)의 포상금 추가 +1
                answer[idx] += 1

    return answer


# [2,1,1,0]
print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
        2
    )
)

# [0,0]
print(
    solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
)



