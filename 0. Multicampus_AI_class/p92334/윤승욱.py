
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
    for from_to in report

    return answer



# [2,1,1,0]
print(
    solution(
        ["muzi", "frodo", "apeach", "neo"]
        ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
        2
    )
)

# [0,0]
print(
    solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con" ], 3)
)


