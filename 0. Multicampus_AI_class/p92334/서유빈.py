
# id_list는 이용자의 ID가 담긴 문자열 배열 (ex) ["con", "ryan"]
# report는 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 (ex) ["ryan con", "ryan con", "ryan con", "ryan con"]
# k는 정지 기준이 되는 신고 횟수 (ex) 3
# answer는 각 유저별로 처리 결과 메일을 받은 횟수
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
            # 신고내역에 추가
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

    user_reported = [] # 신고당한 유저 리스트
    user_banned = [] # 신고당한 유저에서 k이상의 횟수로 신고당해 정지된 유저 리스트
    user_good = [] # 신고한 유저 리스트
    user_list = [] # 유저 리스트 (신고한 사람, 신고당한 사람 포함)

    # user_list에 신고자, 신고당한 사람 insert
    u = report
    users = ' '.join(i for i in report)
    user_list = users.split(' ')

    # user_reported에 신고당한 유저 insert, user_good에 신고한 유저 insert
    user_reported = user_list[1::2]
    user_good = user_list[0::2]

def solution(id_list, report, k):
    answer = []
    reported_people = []  # 신고당한 사람 리스트
    stoped_people = []  # 정지된 사람 리스트 (신고당한 사람 중에서 정지된 사람)
    good_people = []  # 신고 잘 한 사람 리스트

    report = set(report)
    report = list(report)

    for i in range(len(report)):
        tmp = report[i].split(" ")
        reported_people.append(tmp[1])

    for i in range(len(id_list)):
        if reported_people.count(id_list[i]) >= k:
            stoped_people.append(id_list[i])

    for i in range(len(report)):
        tmp = report[i].split(" ")
        if stoped_people.count(tmp[1]) == 1:
            good_people.append(tmp[0])

    for i in range(len(id_list)):
        answer.append(good_people.count(id_list[i]))

    return answer