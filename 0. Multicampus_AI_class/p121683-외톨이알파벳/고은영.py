# 외톨이 판단 기준 : 등장횟수 (2번이상), 구간이 나뉘너져 있는지 여부
# 등장횟수 / 구간을 각각 dictionary 처리

def solution(string):
    dict = {} #각 요소의 등장횟수 dictionary
    visited = {} #각 요소의 구간여부 표시용 dictionary
    for i in list(string):
        visited[i] = False # false 로 초기값 세팅
    result =[]

    #등장횟수 카운팅
    for idx,i in enumerate(list(string)):
        #등장횟수 처리
        try:
            dict[i] += 1
        except:
            dict[i] = 1

        #방문횟수 2이상 및 구간이 True인가? ==> '외톨이 조건'
        if dict[i] >=2 and visited[i]:
          result.append(i)

        #구간 처리
        try:
            if i == list(string)[idx+1]: #다음요소가 동일하면 아직 바꾸지말고
                visited[i] = False
            else: #동일하지 않으면 바꾸기
                visited[i] = True
        except:pass



    if result == [] :
        return 'N'
    else:
        return set(result)




print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))
