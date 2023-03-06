def solution(id_list, report, k):
    dict_num = {}
    #id ,아이디가 신고당한 횟수
    dict_string_list = {}
    # id , 신고한 id string list
    reportuniq = set(report)
    banuser = []
    mail = []

    for i in range(len(id_list)):
        mail.append(0)
        dict_num[id_list[i]] = 0
        dict_string_list[id_list[i]] = []
    #초기화 작업

    for accuse in reportuniq:
        me,you = accuse.split()
        dict_num[you] +=1
        dict_string_list[me].append(you)

    print(dict_num)
    print(dict_string_list)

    for key,value in dict_num.items():
        if value >= k :
            banuser.append(key)

    print(banuser)

    for key,value in dict_string_list.items():
        for v in value:
            if v in banuser:
                mail[id_list.index(key)]+=1


    print(mail)
    return(mail)

#[2,1,1,0]
#[2,1,1,0]
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))

# print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))