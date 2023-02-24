def solution(id_list, report, k):
    answer = []
    # dict * 2
    # list
    # str.split()
    id_list = ["muzi","frodo","apeach","neo"]
    return answer

# 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템 개발
# 동일한 유저에 대한 다중 신고는 1회로 처리됨
# k번 이상 신고된 유저는 게시판 이용 정지되고, 신고한 모든 유저에게 사실 메일 발송





# [2,1,1,0]
print(solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
        2))

# [0,0]
print(solution(
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3)
)