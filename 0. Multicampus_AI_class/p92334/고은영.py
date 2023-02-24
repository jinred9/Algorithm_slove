def solution(id_list, report, k):
     a =[]
     b = []
     answer =[]

     for i in set(report):
         a.append(i.split(' ')[1])

     for j in id_list:
          if a.count(j) >= k:
              b.append(j)

     answer = [i.split()[0] for i in set(report) if i.split()[1] in b]

     return [answer.count(i) for i in id_list]





# [2,1,1,0]
print(solution(
                ["muzi", "frodo", "apeach", "neo"]
               ,["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
               ,2))
# [0,0]
print(solution(
            ["con", "ryan"]
        ,["ryan con", "ryan con", "ryan con", "ryan con"]
        ,3))